"""
A nested NK model. Will fuction like a NK model but in addition a k is specified for
the number of loci used from any gene within an organism.

A genome is composed of a bitstring broken up into multiple genes.
k_intra specifies the number of neighbors within the same gene
k_jump specifies the number of positions to randomly choose within an organism
length_of_gene indicates the length of the subbitstring
number_of_genes specifies the number of subbitstrings within a organism

A contribution_lookup_table is a randomly generated list of list of floats
used to score the fitness of subbitstrings
"""

from nk_organism import Organism
import random
import nk_model
from bitstring import Bitstring
random_generator = random.Random()


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
           self.contribution_lookup_table = nk_model.generate_contribution_lookup_table(
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
        for i in range(len(whole_bitstring)/self.length_of_gene):
            gene_holder.append(Bitstring(whole_bitstring[i * self.length_of_gene:(i + 1) 
                                                  * self.length_of_gene]))
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
                location = (random_generator.randrange(number_of_genes),
                            random_generator.randrange(length_of_gene))
                while location in dependencies[i]:
                    location = (random_generator.randrange(number_of_genes), 
                                random_generator.randrange(length_of_gene))
                dependencies[i][j].append(location)
                                 
    return dependencies

def generate_sub_bitstring(bitstrings, dependencies, k_intra):
    """
    Chooses k_intra random bits from any bitstring (including own)
    and appends them onto the normal nk model sub-bit
    """
    basic_strings = [nk_model.deconstruct_bitstring(single_bit, k_intra)
                     for single_bit in bitstrings]
    complex_strings = []
    for i in range(len(basic_strings)):
        subbit = []
        for j in range(len(basic_strings[i])):
            orglist  = list(basic_strings[i][j])
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
    basic_strings = [nk_model.deconstruct_bitstring(single_bit, k_intra)
                     for single_bit in bitstrings]

    complex_strings = []
    for i in range(len(basic_strings)):
        subbit = []
        for j in range(len(basic_strings[i])):
            orglist = list(basic_strings[i][j])
            toadd = []
            for org in range(i+1, i+k_jump+1):
                toadd.append(bitstrings[org%len(bitstrings)][j])
            orglist.extend(toadd)
            subbit.append(Bitstring(orglist))
        complex_strings.append(subbit)
    return complex_strings
    
