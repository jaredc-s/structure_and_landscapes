"""
Mutate module implements different ways of mutating genome
representations.

random_generator attribute allows MockRandom swapping
"""
import random
import bitstring

random_generator = random.Random()


def mutate_value(value, mutation_rate = 1.0):
    """
    mutate_values if the random number is less than mutation_rate (defaults to always)
    currently handles:
    1: ints
    2: bitstrings
    3: str (RNAs)
    """
    if random_generator.random() < mutation_rate:
        return _get_mutant_value(value)
    return value


def _get_mutant_value(value):
    if isinstance(value, int):
        return shift_by_one(value)
    elif isinstance(value, bitstring.Bitstring):
        return flip_single_bit(value)
    elif isinstance(value, str):
        return change_single_base(value)
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


def change_single_base(sequence):
    """changes a single base in a sequence"""
    possibilities = ['G', 'C', 'A', 'T']
    position = random_generator.randrange(len(sequence))
    print(possibilities)
    print(sequence[position])
    possibilities.remove(sequence[position])
    mutate_to = random_generator.choice(possibilities)
    return sequence[:position] + mutate_to + sequence[position + 1:]
