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

def save(filepath, key, value):
    shelf = shelve.open(filepath, flag='c', protocol=pickle.HIGHEST_PROTOCOL)
    shelf[key] = value
    shelf.close()

def load(filepath, key):
    shelf = shelve.open(filepath, flag='r', protocol=pickle.HIGHEST_PROTOCOL)
    result = shelf[key]
    shelf.close()
    return result
