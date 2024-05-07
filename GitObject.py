class GitObject:

    def __init__(self, data=None):
        if data != None:
            self.deserialize(data)

    def serialize(self):
        raise Exception("Unimplemented")

    def deserialize(self):
        raise Exception("Unimplemented")


class GitBlob(GitObject):
    fmt = b'blob'
    data = None

    def serialize(self):
        return self.data

    def deserialize(self, data):
        self.data = data
