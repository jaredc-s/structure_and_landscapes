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
        if self.contribution_lookup_table is None:
           self.contribution_lookup_table = 
           nk_model.generate_contribution_lookup_table(self.length_of_genome,
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
