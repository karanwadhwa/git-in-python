import argparse
import Commands


def main():
    parser = argparse.ArgumentParser(
        description='wannabe git written in python')
    subparser = parser.add_subparsers(
        title='Commands', dest='command', required=True, help='use a command')

    init_parser = subparser.add_parser(
        'init', help='Create an empty git repository or reinitialize an existing one')
    init_parser.add_argument("path", metavar="directory", default=".", nargs="?",
                             help="Directory path to create the git repository")
    init_parser.set_defaults(func=Commands.init)

    args = parser.parse_args()
    args.func(args)
