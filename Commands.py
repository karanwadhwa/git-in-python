from GitRepository import GitRepository


def init(args):
    repo = GitRepository(args.path, force=True)
    repo.initialize()
    print(repo)
