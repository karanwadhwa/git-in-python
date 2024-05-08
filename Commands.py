import os
import sys
from GitRepository import GitRepository
from GitObject import GitBlob
from utils import repo_find


def init(args):
    repo = GitRepository(args.path, force=True)
    repo.initialize()
    print(repo)


def cat_file(args):
    repo = repo_find()
    obj = repo.object_read(args.object)
    sys.stdout.buffer.write(obj.serialize())


def hash_obj(args):
    realpath = os.path.realpath(args.path)
    with open(realpath, 'rb') as f:
        data = f.read()
        blob = GitBlob(data)
        repo = repo_find()
        sha = repo.object_write(blob, write=args.write == "True")
        print(sha)
