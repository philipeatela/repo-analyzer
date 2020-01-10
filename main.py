from git import Repo
import git
import os
import sys
import collections
import utils

repo_path = sys.argv[1]
print('Running repo-analyzer for ' + repo_path + '...')

repo_name = utils.getRepoName(repo_path)

if(not os.path.exists('/' + repo_name)):
  Repo.clone_from(repo_path, os.getcwd() + '/' + repo_name)

