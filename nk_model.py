"""
Implementation of Stuart Kauffman's NK Model.

Genomes are bitstrings of length "n".
The number of epistatic neighbors of a loci is denoted "k".

When k = 0, the adaptive landscape is smooth.
When k = n - 1, the landscape is maximally rugged.

Every locus in the bitstring has a respective function requiring
the state of the locus and its "k" neighbors (those immediately
following with wrapping about ends).

The outcome of each function is drawn from a  uniformly
distribution. The mean contribution of each locus is the fitness.
"""
from random import Random
from bitstring import Bitstring
module_random_generator = Random()


class NKModel(object):
    """
    Class which is used to evaluate the fitness of a bitstring.
    """
    def __init__(self, n=2, k=0, contribution_lookup_table=None, inner_dependcies=None):
        """
        NKModel instances default to a simple smooth landscape (n=2, k=0),
        and using the module's random number generator (seeded by time).
        """
        self.n = n
        self.k = k
        if contribution_lookup_table is None:
            contribution_lookup_table = generate_contribution_lookup_table(
                self.n, self.k)

        self.contribution_lookup_table = contribution_lookup_table
        
        if inner_dependcies is None:
            inner_dependcies = determine_inner_dependencies(self.n, self.k)
        
        self.inner_dependcies = inner_dependcies

    def determine_fitness(self, bitstring):
        """
        Takes a bitstring and computes a floating point fitness
        """
        contribs = [table[int(sub)] for sub, table in zip(
            deconstruct_bitstring(bitstring, self.k),
            self.contribution_lookup_table)]
        return sum(contribs) / float(len(contribs))

    def determine_fitness_from_random(self, bitstring):
        """
        Takes a bitstring and computes floating point fitness
        from a subset of random bitstrings of length k+1
        """
        contribs = [table[int(sub)] for sub, table in zip(
                decontruct_random_bitstring(bitstring, self.dependencies),
                self.contribution_lookup_table)]
        return sum(contribs) / float(len(contribs))

def deconstruct_bitstring(bitstring, k):
    """
    Takes a bitstring and breaks into a list of sub bitstrings
    with each item starting at a given locus and including the next
    k elements.
    """
    return [get_substring_with_wrapping(
        bitstring, k, i) for i in range(len(bitstring))]

def decontruct_random_bitstring(bitstring, dependencies):
    """
    For use when k loci are not spacially attatched
    Breaks bitstring into a list of sub bitstrings
    where the next k elements are randomly separated
    around bitstring
    """
    return [get_random_substring(bitstring, i, dependencies) 
            for i in range(len(bitstring))]

def get_random_substring(bitstring, i, dependencies):
    """
    Takes a bitstring, k and an index, breaks the bitstring
    into a list of length k+1 where the first index is the 
    value found at i and the remaining k values are chosen
    at random from remainder of bitstring
    """
    bitstring_as_list = list(bitstring)
    bit_values = [bitstring_as_list[locus] for locus in dependencies[i]]
    return Bitstring(bit_values)

def determine_inner_dependencies(n, k):
    """
    Returns related loci within a bitstring for use with a random
    model
    """
    depends = []
    for i in range(n):
        positions = [i]
        #need to remove the initial index so is not dependent on self twice
        r = range(n)
        r.remove(i)
        positions.extend(module_random_generator.sample(r, k))
        depends.append(positions)
    return depends
            

def get_substring_with_wrapping(bitstring, k, i):
    """
    Takes a bitstring, k and index, breaking the bitstring into a sub
    bitstring by the index to index + k. If neighbors go past the end
    it wraps to the beginning of the bitstring.

    ex.
    bitstring = '11100'
    k = 3
    i = 2
    returns '1001'
    """
    if i + k >= len(bitstring):
        bitstring_as_list = list(bitstring[i:])
        postwrap = list(bitstring[:(i + k) - len(bitstring) + 1])
        bitstring_as_list.extend(postwrap)
        return Bitstring(bitstring_as_list)
    else:
        return Bitstring(bitstring[i: k + i + 1])


def generate_contribution_lookup_table(
        n, k, random_generator=module_random_generator):
    """
    Fitness is the mean of the contribution of each loci.
    Each loci has its own lookup table composed of 2 ** (k + 1) uniformly
    distributed entries corresponding to the numerical value of the
    subbitstring (locus + k neighbors).
    """
    return [[random_generator.random() for _ in range(2 ** (k + 1))]
            for _ in range(n)]
