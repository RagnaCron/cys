import os
import argparse

parser = argparse.ArgumentParser(
    description="Clean up directory and put files into according folders."
)

parser.add_argument(
    "--path",
    type=str,
    default=".",
    help="Directory path of the to be cleaned directory",
)

# parse the arguments given by the user and extract the path
args = parser.parse_args()
path = args.path

print(f"Cleaning up directory {path}")
