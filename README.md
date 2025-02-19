GitHub Repository Visibility Switcher

Overview

This script allows you to programmatically update the visibility (public or private) of multiple GitHub repositories that start with a specific substring.

Prerequisites

Ensure you have the following installed:

Python 3.x

pip (Python package manager)

A GitHub Personal Access Token (PAT) with repo permissions

Setup Instructions

1. Clone the Repository

 git clone <your-repo-url>
 cd <your-repo-folder>

2. Create a Virtual Environment (Recommended)

python3 -m venv venv

3. Activate the Virtual Environment

On macOS/Linux:

source venv/bin/activate

On Windows (PowerShell):

venv\Scripts\Activate

On Windows (Command Prompt):

venv\Scripts\activate

4. Install Dependencies

pip install -r requirements.txt

5. Run the Script

python script_name.py

6. Enter Your GitHub Credentials

When prompted, enter:

Your GitHub Username

Your GitHub Personal Access Token

Choose whether to set repositories to public or private

Troubleshooting

Issue: Import "requests" missing issues

Ensure you're in the virtual environment (venv activated).

Run pip install requests again.

Issue: source venv/bin/activate: No such file or directory

Ensure you've created the virtual environment with python3 -m venv venv.

Check if the venv/ folder exists in your project directory.

Issue: Running script in VS Code fails with null error

Try running python script_name.py directly from the terminal.

License

This project is open-source. Feel free to modify and distribute it!
