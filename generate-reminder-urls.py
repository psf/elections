"""Script to convert election id and email address(es) to reminder Email URL.

The desired output is a list of URLs for someone to use to send individual
emails.
"""
import argparse
import collections
import csv
import uuid


Voter = collections.namedtuple('Voter', 'id, email, name')


def create_parser():
    """Create an argument parser."""
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--election', dest='election_id',
        type=uuid.UUID,
        help='Election UUID',
    )
    parser.add_argument(
        '--voter-file', dest='voter_file',
        type=argparse.FileType('r'),
        help='List of voters in Helios CSV bulk upload format',
    )
    parser.add_argument(
        'emails',
        nargs=argparse.REMAINDER,
        help='email addresses of voters',
    )
    return parser


def main():
    """Generate the URLs."""
    parser = create_parser()
    args = parser.parse_args()
    helios_list = csv.reader(args.voter_file, delimiter=',')
    voters_list = [Voter(*row) for row in helios_list]
    voters_by_email = {voter.email: voter for voter in voters_list}
    election_id = str(args.election_id)
    for email in args.emails:
        try:
            voter = voters_by_email[email]
        except KeyError:
            print(f'No voter with email "{email}"')
        else:
            print(f'https://vote.heliosvoting.org/helios/elections/{election_id}/voters/email?voter_id={voter.id}')


if __name__ == '__main__':
    main()
