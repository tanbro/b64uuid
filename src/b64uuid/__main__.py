#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Generate a base64 encoded URL safe UUID
"""

from argparse import ArgumentParser

from .b64uuid import B64UUID


def get_args():
    parser = ArgumentParser(prog='b64uuid', description=__doc__)
    parser.add_argument(
        '--uuid', '-u', type=str,
        help='Generate short ID from the UUID hex string'
             'Can not be used together with "--short-id".'
             '(default=%(default)s)'
    )
    parser.add_argument(
        '--short-id', '-s', type=str,
        help='Reversely convert short ID to UUID. '
             'Can not be used together with "--uuid".'
             '(default=%(default)s)'
    )
    return parser.parse_args()


def main():
    args = get_args()

    if args.uuid:
        print(B64UUID(args.uuid).string)
    elif args.short_id:
        print(str(B64UUID(args.short_id).uuid))
    else:
        print(B64UUID().string)


if __name__ == '__main__':
    main()
