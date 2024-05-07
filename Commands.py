import sys
from GitRepository import GitRepository
from utils import repo_find


def init(args):
    repo = GitRepository(args.path, force=True)
    repo.initialize()
    print(repo)


def cat_file(args):
    repo = repo_find()
    obj = repo.object_read(args.object)
    sys.stdout.buffer.write(obj.serialize())
