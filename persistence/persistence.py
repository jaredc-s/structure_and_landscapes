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
    with closing(get_shelf(filepath)) as shelf:
        shelf[key] = value

def load(filepath, key):
    with closing(get_shelf(filepath)) as shelf:
        return shelf[key]

def get_shelf(filepath):
    """
    Returns the shelf object. Don't forget to close.
    """
    return shelve.open(filepath, flag='c', protocol=pickle.HIGHEST_PROTOCOL)

def save_with_unique_key(filepath, value):
    """
    Saves a given object with a unique key.
    """
    key = str(uuid.uuid4())
    save(filepath, key, value)
