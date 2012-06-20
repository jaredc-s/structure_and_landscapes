"""
Mutate module implements different ways of mutating genome
representations.

random_generator attribute allows MockRandom swapping
"""
import random
import bitstring

random_generator = random.Random()


def mutate_value(value):
    """
    mutate_values knowns ints and Bitstrings so far"
    """
    if isinstance(value, int):
        return shift_by_one(value)
    elif isinstance(value, bitstring.Bitstring):
        return flip_single_bit(value)
    else:
        raise TypeError("unknown type to mutate")


def shift_by_one(number):
    """
    increments or decrements integer
    """
    if random_generator.random() < 0.5:
        return number + 1
    else:
        return number - 1


def flip_single_bit(bitstring_):
    """
    flips a single position in the bitstring
    """
    position = random_generator.randrange(len(bitstring_))
    return bitstring.flip_positions(bitstring_, [position])
