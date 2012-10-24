#!/usr/bin/env python2
import random
import argparse
from persistence.run import process_and_run


parser = argparse.ArgumentParser(
        description="Command Line Interface for the structure and landscapes package.")
parser.add_argument('--parameters', help="specify the location of the configuration file")
parser.add_argument('--seed', dest='seed', type=int, help="random number seed, default to current time")
args = parser.parse_args()

random.seed(args.seed)

parameter_settings = {}
with open(args.parameters, "r") as parameters_file:
    for line in parameters_file:
        line_without_comments, _, _ = line.partition("#")
        line_stripped = line_without_comments.strip()
        if not line_stripped:
            continue
        parameter, _, value = line_stripped.partition(":")
        parameter_settings[parameter] = value

process_and_run(parameter_settings)
