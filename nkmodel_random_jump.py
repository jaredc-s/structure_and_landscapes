from nk_organism import Organism
import random
import nk_model


random_generator = random.Random()

class NKWithGenes(object):
    def __init__(self, k_intra, k_jump, length_of_gene,
                 number_of_genes, contribution_lookup_table=None):
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

        self.dependencies = generate_dependencies(self.number_of_genes,
                                                  self.length_of_gene, self.k_jump)

    def determine_fitness(self, list_of_bitstrings):
        """
        grab value at each k+1 loci
        look in dependency table for the allied loci
        look in bitstring for values at loci
        append values 
        look in contrib table to determine fitness
        primary_bit = 
        """
        pass

def generate_dependencies(number_of_genes, length_of_gene, k_jump):
    """
    Function takes in each independent gene and returns
    a list of dependencies based off locus for each gene
    """
    dependencies = []
    for _ in range(number_of_genes):
        dependencies.append([(random_generator.randrange(number_of_genes), 
                                 random_generator.randrange(length_of_gene))
                             for _ in range(k_jump)])
    return dependencies
