"""
Mutate module implements different ways of mutating genome
representations.

random_generator attribute allows MockRandom swapping
"""
import random
import bitstring

random_generator = random.Random()


def mutate_value(value, mutation_rate = 0.2):
    """
    mutate_values knowns ints and Bitstrings so far"
    """
    if isinstance(value, int):
        return shift_by_one(value)
    elif isinstance(value, bitstring.Bitstring):
        return flip_single_bit(value)
    elif isinstance(value, str):
        return change_single_base(value)
    else:
        raise TypeError("unknown type to mutate")
    if random_generator.random() < mutation_rate:
        if isinstance(value, int):
            return shift_by_one(value)
        elif isinstance(value, bitstring.Bitstring):
            return flip_single_bit(value)
        elif isinstance(value, RS.RNAsequence):
            return change_single_base(value)
        else:
            raise TypeError("unknown type to mutate")
    else:
        return value

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
    possibilities = ['G', 'C', 'A', 'U']
    position = random_generator.randrange(len(sequence))
    possibilities.remove(sequence[position])
    mutate_to = random_generator.choice(possibilities)
    return sequence[:position] + mutate_to + sequence[position + 1:]
