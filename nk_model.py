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
    def __init__(self, n=2, k=0, contribution_lookup_table=None,
                 inner_dependencies=None):
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

        if inner_dependencies is None:
            inner_dependencies = determine_inner_dependencies(self.n, self.k)

        self.inner_dependencies = inner_dependencies

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
                    decontruct_random_bitstring(bitstring, self.inner_dependencies),
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



"""
A nested NK model. Will fuction like a NK model
but in addition a k is specified forthe number of
loci used from any gene within an organism.

A genome is composed of a bitstring broken up into multiple genes.
k_intra specifies the number of neighbors within the same gene
k_jump specifies the number of positions to randomly choose within an organism
length_of_gene indicates the length of the subbitstring
number_of_genes specifies the number of subbitstrings within a organism

A contribution_lookup_table is a randomly generated list of list of floats
used to score the fitness of subbitstrings
"""

class NKWithGenes(object):

    def __init__(self, k_intra, k_jump, length_of_gene,
                 number_of_genes, contribution_lookup_table=None):
        """
        Takes a k for neighbors within a starting gene, a k for any gene,
        a length of gene, the number of genes and a contribution lookuptable.
        """

        self.k_intra = k_intra
        self.k_jump = k_jump
        self.length_of_gene = length_of_gene
        self.number_of_genes = number_of_genes
        self.length_of_genome = self.length_of_gene * self.number_of_genes
        if contribution_lookup_table is None:
            self.contribution_lookup_table = generate_contribution_lookup_table(
                self.length_of_genome, self.k_intra + self.k_jump)
        else:
            self.contribution_lookup_table = contribution_lookup_table

        self.dependencies = generate_dependencies(self.k_intra, self.k_jump,
                                                  self.number_of_genes,
                                                  self.length_of_gene)

    def determine_fitness(self, bitstring):
        """
        grab value at each k+1 loci
        look in dependency table for the allied loci
        look in bitstring for values at loci
        append values
        look in contrib table to determine fitness
        """
        genes = self.divide_to_genes(bitstring)
        contribs = []
        each_org = []
        sub_bits = generate_sub_bitstring(genes, self.dependencies,
                                          self.k_intra)
        for orgs in sub_bits:
            each_org.extend(orgs)
        for sub, table in zip(each_org, self.contribution_lookup_table):
            contribs.extend([table[int(sub)]])
        return sum(contribs) / float(len(contribs))

    def divide_to_genes(self, whole_bitstring):
        gene_holder = []
        for i in range(len(whole_bitstring) / self.length_of_gene):
            gene_holder.append(Bitstring(whole_bitstring[i *
                               self.length_of_gene:(i + 1) *
                               self.length_of_gene]))
        return gene_holder


def generate_dependencies(k_intra, k_jump, number_of_genes, length_of_gene):
    """
    Function takes in each independent gene and returns
    a list of dependencies based off locus for each gene
    Random gene and random loci
    """
    dependencies = []
    for i in range(number_of_genes):
        dependencies.append([])
        for j in range(length_of_gene):
            dependencies[i].append([])
            for _ in range(k_jump):
                location = (module_random_generator.randrange(number_of_genes),
                            module_random_generator.randrange(length_of_gene))
                while location in dependencies[i][j]:
                    location = (module_random_generator.randrange(number_of_genes),
                                module_random_generator.randrange(length_of_gene))
                dependencies[i][j].append(location)

    return dependencies


def generate_sub_bitstring(bitstrings, dependencies, k_intra):
    """
    Chooses k_intra random bits from any bitstring (including own)
    and appends them onto the normal nk model sub-bit
    """
    basic_strings = [deconstruct_bitstring(single_bit, k_intra)
                     for single_bit in bitstrings]
    complex_strings = []
    for i in range(len(basic_strings)):
        subbit = []
        for j in range(len(basic_strings[i])):
            orglist = list(basic_strings[i][j])
            dependent = dependencies[i][j]
            for org, pos in dependent:
                hold = bitstrings[org][pos]
                orglist.append(hold)

            subbit.append(Bitstring(orglist))
        complex_strings.append(subbit)
    return complex_strings


def generate_linear_bistring(bitstrings, k_intra, k_jump):
    """
    Generates standard nk model and appends value at starting locus
    in the next k_intra genes

    ex. n = 3 genes = 3 k_in = 2 k_out = 2
    gene1:101 gene2:010 gene3:100

    bitstring1: 10101
    bitstring2: 01110
    bitstring3: 11000
    """
    basic_strings = [deconstruct_bitstring(single_bit, k_intra)
                     for single_bit in bitstrings]

    complex_strings = []
    for i in range(len(basic_strings)):
        subbit = []
        for j in range(len(basic_strings[i])):
            orglist = list(basic_strings[i][j])
            toadd = []
            for org in range(i + 1, i + k_jump + 1):
                toadd.append(bitstrings[org%len(bitstrings)][j])
            orglist.extend(toadd)
            subbit.append(Bitstring(orglist))
        complex_strings.append(subbit)
    return complex_strings
