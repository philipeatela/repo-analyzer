from git import Repo
import git
import os
import sys
import collections
import utils

ANALYZED_BRANCH = 'master'

repo_url = sys.argv[1]
print('Running repo-analyzer for ' + repo_url + '...')

repo_name = utils.getRepoName(repo_url)
repo_destination = os.getcwd() + '/' + repo_name
repo_dir = os.path.isdir(repo_destination)

print(repo_dir)
print('the repository exists?', repo_dir)

if(repo_dir):
  repo = Repo(repo_destination)
else:
  repo = Repo.clone_from(repo_url, repo_destination)

all_commits = list(repo.iter_commits(ANALYZED_BRANCH))

print(len(all_commits))
for commit in all_commits:
  print('Author: ', str(commit.author))
  print('Author: ', str(commit.author.email))
  print('Author: ', str(commit.message))