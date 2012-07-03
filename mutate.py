"""
Mutate module implements different ways of mutating genome
representations.

random_generator attribute allows MockRandom swapping
"""
import random
import bitstring
import RNA_Sequence as RS

random_generator = random.Random()


def mutate_value(value, mutation_rate = 0.2):
    """
    mutate_values knowns ints and Bitstrings so far"
    """
    if isinstance(value, int):
        return shift_by_one(value, mutation_rate)
    elif isinstance(value, bitstring.Bitstring):
        return flip_single_bit(value, mutation_rate)
    elif isinstance(value, RS.RNAsequence):
        return change_single_base(value, mutation_rate)
    else:
        raise TypeError("unknown type to mutate")


def shift_by_one(number, mutation_rate):
    """
    increments or decrements integer
    """
    if random_generator.random() < mutation_rate:
        return number + 1
    else:
        return number - 1


def flip_single_bit(bitstring_, mutation_rate):
    """
    flips a single position in the bitstring
    """
    if random_generator.random() < mutation_rate:
        position = random_generator.randrange(len(bitstring_))
        return bitstring.flip_positions(bitstring_, [position])
    else:
        return bitstring_

def change_single_base(sequence, mutation_rate):
    """changes a single base in a sequence"""
    if random_generator.random() < mutation_rate:
        position = random_generator.randrange(len(sequence))
        return RS.change_base(sequence, [position])
    else:
        return sequence
