#!/usr/bin/env python2
import random
from persistence.run import process_and_run

random.seed(1)

parameter_settings = {}
with open("parameters.cfg") as parameters_file:
    for line in parameters_file:
        line_without_comments, _, _ = line.partition("#")
        line_stripped = line_without_comments.strip()
        if not line_stripped:
            continue
        parameter, _, value = line_stripped.partition(":")
        parameter_settings[parameter] = value

process_and_run(parameter_settings)
