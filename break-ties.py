#!/usr/bin/env python3

"""Utility script for breaking ties in PSF Board of Directors elections."""

import argparse
import random


def parser():
    """Create an ArgumentParser."""
    argparser = argparse.ArgumentParser()
    argparser.add_argument(
        '-c', '--candidate',
        action='append',
        dest='candidates',
        help='Name of candidate in tie',
    )
    argparser.add_argument(
        '-n', '--number',
        type=int,
        dest='number',
        default=1,
        help="Number of candidates to select"
    )
    return argparser


def main():
    """Control main execution of script."""
    argparser = parser()
    arguments = argparser.parse_args()
    candidates = sorted(arguments.candidates)
    random.seed(''.join(candidates))
    print(random.sample(candidates, arguments.number))

if __name__ == '__main__':
    main()
