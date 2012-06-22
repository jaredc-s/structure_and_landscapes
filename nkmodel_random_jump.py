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
        if self.contribution_lookup_table is None:
           self.contribution_lookup_table =
           nk_model.generate_contribution_lookup_table(self.length_of_gene * self.number_of_genes,
                                                       self.k_intra + self.k_jump)

def generate_dependencies(number_of_genes, length_of_genome, k_jump):
    """
    Function takes in each independent gene and returns
    a list of dependencies based off locus for each gene
    """
    dependencies = []
    for _ in number_of_genes:
        dependencies.append([random_generator.randrange(length_of_genome)
                             for _ in range(k_jump)])
    return dependencies
