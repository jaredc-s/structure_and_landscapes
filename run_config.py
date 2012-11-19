#!/usr/bin/env python2
import random
import argparse
from persistence.run import process_and_run
import datetime

parser = argparse.ArgumentParser(
        description="Command Line Interface for the structure and landscapes package.")
parser.add_argument('--parameters', help="specify the location of the configuration file")
parser.add_argument('--seed', default=0, type=int, help="random number seed, default to current time")
parser.add_argument('--number_of_runs', default=1, type=int, help="the specified number of runs")
args = parser.parse_args()

random.seed(args.seed)
args.number_of_runs

def get_parameter_settings(parameters_file_path):
    """
    Parse parameters file.
    Comments are after '#' symbols. 'xxx:yyy' are the key-value mappings.
    If multiple settings are included ('xxx:y,z'), then the full factorial of all multiple
    settings are returned, as multiple dictionaries.
    """
    parameter_settings = {}
    with open(parameters_file_path, "r") as parameters_file:
        multiple_values = {}
        parameter_settings['Seed'] = args.seed
        for line in parameters_file:
            line_without_comments, _, _ = line.partition("#")
            line_stripped = line_without_comments.strip()
            if not line_stripped:
                continue
            parameter, _, value = line_stripped.partition(":")
            values_split = value.split(",")
            if len(values_split) == 1:
                parameter_settings[parameter] = value
            else:
                multiple_values[parameter] = [value_split.strip() for value_split in values_split]

        all_parameter_settings = []
        for parameter, value_list in multiple_values:
            for value in value_list:
                specific_parameter_settings = parameter_settings.copy()


        return all_parameter_settings

parameter_settings = get_parameter_settings(args.parameters)

if args.seed != 0 and args.number_of_runs > 1:
    raise AssertionError("cannot specify a seed and more than one run at the same time")

for _ in range(args.number_of_runs):
    parameter_settings['Time Started'] = datetime.datetime.now()
    process_and_run(parameter_settings)
