import os
import configparser


class GitRepository():
    '''
    A git repository

    path: path to repository (worktree)
    force: disables all checks
    '''

    worktree = None
    gitdir = None
    config = None

    def __init__(self, path, force=False):
        self.worktree = os.path.realpath(path)
        self.gitdir = os.path.join(self.worktree, '.git')

        # Check if worktree exists
        if os.path.exists(self.worktree) and not os.path.isdir(self.worktree):
            raise Exception(
                f'Cannot initialize repo at path: {self.worktree}. File already exists.')

        # Check if .git dir has been initialized
        if not (force or os.path.isdir(self.gitdir)):
            raise Exception(f'Err: Not a git repository {path}')

        # Read git config
        self.config = configparser.ConfigParser()
        config_path = os.path.join(self.gitdir, 'config')

        if config_path and os.path.isfile(config_path):
            self.config.read([config_path])
        elif not force:
            raise Exception("git config file missing")

        if not force:
            repositoryformatversion = int(
                self.config.get('core', 'repositoryformatversion'))
            if repositoryformatversion != 0:
                raise Exception(
                    f'unsupported repositoryformatversion: {repositoryformatversion}')

    def __str__(self) -> str:
        return self.worktree

    def _get_path(self, *path) -> str:
        '''Get absolute path under repos gitdir'''
        return os.path.join(self.gitdir, *path)

    def get_file_path(self, *path, mkdir=False):
        '''Create dir *path if absent and return file path'''
        if self.get_dir_path(*path[:-1], mkdir=mkdir):
            return self._get_path(*path)

    def get_dir_path(self, *path, mkdir=False) -> str | None:
        '''Return absolute path of a directory in gitdir. Create dir if it does not exist'''
        path = self._get_path(*path)
        if os.path.exists(path):
            if os.path.isdir(path):
                return path
            else:
                raise Exception(f'{path} is not a directory')
        elif mkdir:
            os.makedirs(path)
            return path
        else:
            return None

    def initialize(self):
        if os.path.exists(self.gitdir) and os.listdir(self.gitdir):
            print("Already initialized as a .git repository. Skipping...")
            return

        # create worktree if it does not exist
        os.makedirs(self.worktree, exist_ok=True)

        # create .git folder if it does not exist
        os.makedirs(self.gitdir, exist_ok=True)

        # populate .git folder
        assert self.get_dir_path("branches", mkdir=True)
        assert self.get_dir_path("objects", mkdir=True)
        assert self.get_dir_path("refs", "tags", mkdir=True)
        assert self.get_dir_path("refs", "heads", mkdir=True)

        with open(self.get_file_path("HEAD"), "w") as f:
            f.write("ref: refs/heads/main\n")

        with open(self.get_file_path("description"), "w") as f:
            f.write(
                "Unnamed repository; edit this file 'description' to name the repository.\n")

        # create and update git config file
        with open(self.get_file_path("config"), "w") as f:
            self.config.add_section('core')
            self.config.set("core", "repositoryformatversion", "0")
            self.config.set("core", "filemode", "false")
            self.config.set("core", "bare", "false")
            self.config.write(f)
