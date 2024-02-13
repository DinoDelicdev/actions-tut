from github import Github
import os


g = Github(os.environ['GH_ACCESS_TOKEN'])

# Replace 'your_username' and 'your_repository' with your GitHub username and repository name
repo = g.get_repo("DinoDelicdev/actions-tut")

branch = repo.get_branch(repo.default_branch)

# Get the most recent commit on the default branch
commit = branch.commit

# Get the list of files changed in the commit
files_changed = commit.files

# Print the list of changed files
for file in files_changed:
    print(file.filename)