"""Script to convert voter data for Helios Voting.

This script expects a CSV generated from an Excel/Google Docs export based
off of CivicCRM data.

The format of the CSV is vaguely: firstname,lastname,email

The desired output for Helios is: uniqueid,email,name
"""
import argparse
import csv
import uuid


def generate_unique_id():
    """Create a UUID for our voter."""
    return uuid.uuid4().hex


def create_parser():
    """Create our argument parser."""
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--from', dest='source',
        type=argparse.FileType('r'),
        help='CSV file based on CivicCRM data',
    )
    parser.add_argument(
        '--to', dest='destination',
        type=argparse.FileType('w'),
        help='CSV file based on CivicCRM data',
    )
    return parser


def convert(from_source, to_destination):
    """Handle conversion of the data."""
    civicrm_reader = csv.reader(from_source, delimiter=',')
    helios_writer = csv.writer(to_destination, delimiter=',')
    for row in civicrm_reader:
        row = [col.strip() for col in row]
        email = row.pop()
        name = ' '.join(row)
        id = generate_unique_id()
        helios_writer.writerow([id, email, name])


def main():
    """Run the conversion."""
    parser = create_parser()
    args = parser.parse_args()
    convert(args.source, args.destination)


if __name__ == '__main__':
    main()
