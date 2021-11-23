#!/usr/bin/env python3
"""
Application description to show on --help
"""
import argparse
import logging
import sys
import warnings

from . import BaseClass, base_function  # pragma: no cover

warnings.simplefilter(action='ignore', category=FutureWarning)
database_name = "mydb.db"


def main():
    parser = argparse.ArgumentParser(
        prog='PROG', description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="See '<command> --help' to read about a specific sub-command.")
    parser.add_argument(
        "-v", "--verbosity", type=str, default='ERROR',
        choices=['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'],
        help="Sets the logging level (default: %(default)s)")
    subparsers = parser.add_subparsers(dest='command', help='Sub-commands')

    # Arguments for subcommand ADD
    add_parser = subparsers.add_parser('add', help='ADD help text')
    add_parser.set_defaults(func=add_command)
    add_parser.add_argument(
        "key", nargs=1, type=str,
        action='store',
        help="Key used to identify the stored value")
    add_parser.add_argument(
        "value",
        action='store', nargs=1, type=str,
        help="Value to store in the database")

    # Arguments for subcommand GET
    get_parser = subparsers.add_parser('get', help='GET help text')
    get_parser.set_defaults(func=get_command)
    get_parser.add_argument(
        "key", nargs=1, type=str,
        action='store',
        help="Key used to identify the value to retrieve")

    # Arguments for subcommand DEL
    del_parser = subparsers.add_parser('del', help='DEL help text')
    del_parser.set_defaults(func=del_command)
    del_parser.add_argument(
        "key", nargs=1, type=str,
        action='store',
        help="Key used to identify the value to delete")

    # Arguments for subcommand LIST
    list_parser = subparsers.add_parser('list', help='LIST help text')
    list_parser.set_defaults(func=list_command)

    # Return arguments
    args = parser.parse_args()
    if args.command is not None:
        run_command(module.Database(), args)
    else:
        parser.print_help()
    sys.exit(0)  # Shell return 0 == success


def run_command(database, args):
    # Set logging level
    logging.basicConfig(
        level=getattr(logging, args.verbosity),
        format='%(asctime)s %(name)-24s %(levelname)-8s %(message)s'
    )

    # Load database
    logging.info("Loading database: %s", database_name)
    try:
        database.load(database_name)
    except FileNotFoundError:
        logging.error("File not found, genereting empty database")

    # Call for function
    args.func(database, args)

    # Saving database
    logging.info("Saving database: %s", database_name)
    database.save("mydb.db")

    # End of program
    logging.info("End of program")


def add_command(database, args):
    logging.debug("Add call with %s, %s", args.key[0], args.value[0])
    database.add(args.key[0], args.value[0])


def get_command(database, args):
    logging.debug("Get call to database with %s", args.key[0])
    print(database.get(args.key[0]))


def del_command(database, args):
    logging.debug("Delete call to database with %s", args.key[0])
    database.delete(args.key[0])


def list_command(database, args):
    logging.debug("Printing database")
    print(database)


if __name__ == '__main__':
    main()
