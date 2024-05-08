import argparse
import Commands


def main():
    parser = argparse.ArgumentParser(
        description='wannabe git written in python')
    subparser = parser.add_subparsers(
        title='Commands',
        dest='command',
        required=True,
        help='use a command')

    # init command
    init_parser = subparser.add_parser(
        'init',
        help='Create an empty git repository or reinitialize an existing one')
    init_parser.add_argument("path",
                             metavar="directory",
                             default=".",
                             nargs="?",
                             help="Directory path to create the git repository")
    init_parser.set_defaults(func=Commands.init)

    # cat-file command
    cat_file_parser = subparser.add_parser(
        'cat-file',
        help="Provide content or type and size information for repository objects")
    cat_file_parser.add_argument("type",
                                 metavar="type",
                                 choices=["blob", "commit", "tag", "tree"],
                                 help="Specify the object type")
    cat_file_parser.add_argument(
        "object",
        metavar="object",
        help="sha1 hash of the object to be displayed")
    cat_file_parser.set_defaults(func=Commands.cat_file)

    # hash-file command
    hash_file_parser = subparser.add_parser(
        'hash-object',
        help="Compute object ID and optionally creates a blob from a file"
    )
    hash_file_parser.add_argument("-w",
                                  dest="write",
                                  action="store_true",
                                  default="False",
                                  help="Actually write the object into the object database")
    hash_file_parser.add_argument("path",
                                  help="Hash object as it were located at the given path")
    hash_file_parser.set_defaults(func=Commands.hash_obj)

    args = parser.parse_args()
    args.func(args)
