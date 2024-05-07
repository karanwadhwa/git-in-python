import os
from GitRepository import GitRepository


def repo_find(repo_path='.'):
    repo_path = os.path.realpath(repo_path)

    if os.path.isdir(os.path.join(repo_path, '.git')):
        return GitRepository(repo_path)

    parent = os.path.realpath(os.path.join(repo_path, '..'))

    # base case - reached root
    if parent == repo_path:
        raise Exception("No git repository found")

    # check recursively
    return repo_find(parent)
