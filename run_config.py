#!/usr/bin/env python2
import random
import argparse
from persistence.run import process_and_run
import datetime
import itertools


def get_parameter_settings(parameters_file_path):
    """
    Parse parameters file.
    Comments are after '#' symbols. 'xxx:yyy' are the key-value mappings.
    If multiple settings are included ('xxx:y,z'), then the full factorial of all multiple
    settings are returned, as multiple dictionaries. Returns a list of parameter settings dictioanries
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

        for specific_values in dictionary_product(multiple_values):
            specific_values.update(parameter_settings)
            all_parameter_settings.append(specific_values)

        return all_parameter_settings

def dictionary_product(key_to_list_of_values):
    """
    takes a dicitonary where each key (string) is a parameter that points
    points to a list of specifications. Returns a flattened list of dictionaries with
    full factorial possibilities of the passed in dictionary.
    """
    keys = key_to_list_of_values.keys()
    values = key_to_list_of_values.values()
    values_product = itertools.product(*values)
    result = []
    for values_tuple in values_product:
        list_of_pairs = zip(keys, values_tuple)
        specific_dict = dict(list_of_pairs)
        result.append(specific_dict)

    return result

if __name__=='__main__':

    parser = argparse.ArgumentParser(
            description="Command Line Interface for the structure and landscapes package.")
    parser.add_argument('--parameters', help="specify the location of the configuration file")
    parser.add_argument('--seed', default=0, type=int, help="random number seed, default to current time")
    parser.add_argument('--number_of_runs', default=1, type=int, help="the specified number of runs")
    args = parser.parse_args()

    random.seed(args.seed)

    parameter_settings = get_parameter_settings(args.parameters)

    if args.seed != 0 and args.number_of_runs > 1:
        raise AssertionError("cannot specify a seed and more than one run at the same time")

    for _ in range(args.number_of_runs):
        for setting in parameter_settings:
            setting['Time_Started'] = datetime.datetime.now()
            process_and_run(setting)
