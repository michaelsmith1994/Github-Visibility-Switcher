import requests

GITHUB_USERNAME = input("Enter your GitHub username: ").strip()
GITHUB_TOKEN = input("Enter your GitHub Personal Access Token: ").strip()
REPO_PREFIX = input("Enter the repository name prefix to filter (e.g., 'michaelsmith1994-'): ").strip()

while True:
    VISIBILITY_CHOICE = input("Do you want to set repositories to 'public' or 'private'? ").strip().lower()
    if VISIBILITY_CHOICE in ["public", "private"]:
        MAKE_PRIVATE = VISIBILITY_CHOICE == "private"
        break
    else:
        print("Invalid choice. Please enter 'public' or 'private'.")

API_URL = "https://api.github.com/user/repos"

HEADERS = {
    "Authorization": f"token {GITHUB_TOKEN}",
    "Accept": "application/vnd.github.v3+json"
}

def get_repositories():
    """Fetch all repositories of the authenticated user"""
    repos = []
    page = 1

    while True:
        response = requests.get(f"{API_URL}?per_page=100&page={page}", headers=HEADERS)
        if response.status_code != 200:
            print(f"Error fetching repos: {response.json()}")
            return []
        
        data = response.json()
        if not data:
            break

        repos.extend(data)
        page += 1  # Go to the next page

    return repos

def update_repo_visibility(repo_name, new_visibility):
    """Update repository visibility to public or private"""
    update_url = f"https://api.github.com/repos/{GITHUB_USERNAME}/{repo_name}"
    payload = {"private": new_visibility}  
    
    response = requests.patch(update_url, json=payload, headers=HEADERS)
    
    if response.status_code == 200:
        print(f"Successfully updated {repo_name} to {'private' if new_visibility else 'public'}")
    else:
        print(f"Failed to update {repo_name}: {response.json()}")

repositories = get_repositories()

for repo in repositories:
    repo_name = repo["name"]
    
    if repo_name.startswith(REPO_PREFIX):
        current_visibility = repo["private"]
        
        if current_visibility == MAKE_PRIVATE:
            print(f"Skipping {repo_name}: Already {'private' if MAKE_PRIVATE else 'public'}")
        else:
            update_repo_visibility(repo_name, MAKE_PRIVATE)
    else:
        print(f"Skipping {repo_name}: Does not match prefix")