"""
Module responsible for saving the results of an evolutionary experiment
Important information to store:

Ancestor
Population Structure
Number of generations
Fitness distribution each generation
Final population
"""
import shelve
import pickle
import uuid
from contextlib import closing


def save(filepath, key, value):
    with get_shelf(filepath) as shelf:
        shelf[key] = value


def load(filepath, key):
    with get_shelf(filepath) as shelf:
        return shelf[key]


def get_shelf(filepath):
    """
    Returns the shelf object. Uses context manager ('with' statement).
    """
    return closing(shelve.open(
        filepath, flag='c', protocol=pickle.HIGHEST_PROTOCOL))


def save_with_unique_key(filepath, value):
    """
    Saves a given object with a unique key.
    """
    key = str(uuid.uuid4())
    save(filepath, key, value)

def values(filepath):
    """
    Given a filepath to a shelve object.
    Returns an iterable of the values contained therein.
    """
    with get_shelf(filepath) as shelf:
        for key in shelf:
            yield shelf[key]

def consolidate(shelf_paths, new_shelf_path):
    """
    Combine contents from iterable of file paths in shelf_paths
    into new_shelf_path.
    """
    with get_shelf(new_shelf_path) as new_shelf:
        for shelf_path in shelf_paths:
            with get_shelf(shelf_path) as old_shelf:
                for key in old_shelf:
                    new_shelf[key] = old_shelf[key]
