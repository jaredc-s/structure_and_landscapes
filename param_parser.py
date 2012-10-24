#!/usr/bin/env python2
import random
import argparse
from persistence.run import process_and_run


parser = argparse.ArgumentParser(
        description="Command Line Interface for the structure and landscapes package.")
parser.add_argument('parameters_file', help="specify the location of the configuration file")
args = parser.parse_args()
print(args)

random.seed(1)


parameter_settings = {}
with open(args.parameters_file, "r") as parameters_file:
    for line in parameters_file:
        line_without_comments, _, _ = line.partition("#")
        line_stripped = line_without_comments.strip()
        if not line_stripped:
            continue
        parameter, _, value = line_stripped.partition(":")
        parameter_settings[parameter] = value

process_and_run(parameter_settings)
