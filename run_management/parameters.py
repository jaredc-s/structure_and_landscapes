import itertools


def get_parameter_settings(parameters_file_contents):
    """
    Returns a list of parameter settings dictionaries corresponding
    to the configuration settings specified (comma seperated values
    are performed in all possible combinations).
    """

    settings = parse_contents_to_settings_dict(parameters_file_contents)
    general_settings, multiple_settings = split_lists_out(settings)

    list_of_settings = []
    for specific_values in dictionary_product(multiple_settings):
        specific_values.update(general_settings)
        list_of_settings.append(specific_values)
    return list_of_settings


def split_lists_out(dictionary):
    """
    Splits given dictionary into two, first the mappings were the value
    is not a list, and the second the mappings whose values are lists.
    """
    without_lists = {}
    with_lists = {}
    for key, value in dictionary.items():
        if isinstance(value, list):
            with_lists[key] = value
        else:
            without_lists[key] = value
    return without_lists, with_lists


def parse_contents_to_settings_dict(parameters_file_contents):
    """
    Parse the contents of the parameters file.
    Comments are after '#' symbols. 'xxx:yyy' are the key-value mappings.
    If multiple settings are included ('xxx:y,z'),
    then the list of values is mapped.
    """
    settings = {}
    for line in parameters_file_contents.splitlines():
        line_without_comments, _, _ = line.partition("#")
        line_stripped = line_without_comments.strip()
        if not line_stripped:
            continue
        raw_parameter, _, raw_value = line_stripped.partition(":")
        parameter = raw_parameter.strip()
        value = raw_value.strip()
        values_split = value.split(",")
        if len(values_split) == 1:
            settings[parameter] = value.strip()
        else:
            settings[parameter] = [value_split.strip()
                                   for value_split in values_split]
    return settings


def dictionary_product(key_to_list_of_values):
    """
    Takes a dicitonary where each key (string) is a parameter that points
    points to a list of specifications.
    Returns a flattened list of dictionaries with
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
