"""Utility script for breaking ties in PSF Board of Directors elections."""
#!/usr/bin/env python3

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
    return argparser


def main():
    """Control main execution of script."""
    argparser = parser()
    arguments = argparser.parse_args()
    print(random.choice(arguments.candidates))
