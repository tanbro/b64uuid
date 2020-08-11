"""
Generate a base64 encoded URL safe UUID
"""

import sys
import os
from argparse import ArgumentParser

from .b64uuid import B64UUID
from .version import version as __version__


PROG = 'b64uuid'


def main():
    prog = PROG
    _, tail = os.path.split(sys.argv[0])
    root, _ = os.path.splitext(tail)
    if root == __name__:
        prog = '{} -m b64uuid'.format(sys.executable)
    parser = ArgumentParser(prog=prog, description=__doc__)
    parser.add_argument(
        '--uuid', '-u', type=str,
        help='Generate short ID from the UUID hex string. '
             'Can not be used together with "--short-id".'
    )
    parser.add_argument(
        '--short-id', '-s', type=str,
        help='Reversely convert short ID to UUID. '
             'Can not be used together with "--uuid".'
    )
    parser.add_argument(
        '--version', '-V', action='version',
        version='%(prog)s {0} from {1} ({2} {3[0]}.{3[1]})'.format(
            __version__, sys.argv[0], sys.implementation.name, sys.version_info
        )
    )
    args = parser.parse_args()

    if args.uuid and args.short_id:
        parser.print_help()
        exit(1)

    if args.uuid:
        print('{}'.format(B64UUID(args.uuid)))
    elif args.short_id:
        print('{}'.format(B64UUID(args.short_id).uuid))
    else:
        print('{}'.format(B64UUID()))


if __name__ == '__main__':
    main()
