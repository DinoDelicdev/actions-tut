from github import Github
import os


g = Github(os.environ['GH_ACCESS_TOKEN'])

# Replace 'your_username' and 'your_repository' with your GitHub username and repository name
repo = g.get_repo("DinoDelicdev/actions-tut")

# Iterate over all commits in the repository
for commit in repo.get_commits():
    # Iterate over all files changed in each commit
    for file in commit.files:
        # Print the filename
        print(file.filename)