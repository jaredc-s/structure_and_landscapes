#!/usr/bin/env python2
import random
import argparse
from structure_and_landscapes.run_management.run import process_and_run
from structure_and_landscapes.run_management.parameters \
    import get_parameter_settings
import datetime


def parse_arguments():
    """
    Parses the command line arguments and returns them
    """
    parser = argparse.ArgumentParser(
        description="Command Line Interface for the "
        "structure and landscapes package.")
    parser.add_argument(
        '--parameters', help="specify the location of the configuration file")
    parser.add_argument(
        '--seed', default=0, type=int,
        help="random number seed, default to current time")
    parser.add_argument(
        '--number_of_runs', default=1, type=int,
        help="the specified number of runs")
    args = parser.parse_args()
    if args.seed != 0 and args.number_of_runs > 1:
        raise AssertionError("cannot specify a seed and "
                             "more than one run at the same time")
    return args


def run_specified_configurations(args):
    """
    Processes the configuration file and performs all runs
    """
    random.seed(args.seed)
    with open(args.parameters, "r") as parameters_file:
        parameters_file_contents = parameters_file.read()

    parameter_settings = get_parameter_settings(parameters_file_contents)
    for _ in range(args.number_of_runs):
        for setting in parameter_settings:
            setting['Time Started'] = datetime.datetime.now()
            process_and_run(setting)


if __name__ == '__main__':
    args = parse_arguments()
    run_specified_configurations(args)
