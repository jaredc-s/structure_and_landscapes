from nk_organism import Organism
import random
import nk_model


class NKWithGenes(object):
    def __init__(self, k_intra, k_jump, length_of_gene,
                 number_of_genes, contribution_lookup_table=None):
        self.k_intra = k_intra
        self.k_jump = k_jump
        self.length_of_gene = length_of_gene
        self.number_of_genes = number_of_genes
        if self.contribution_lookup_table is None:
           self.contribution_lookup_table = 
           nk_model.generate_contribution_lookup_table(self.length_of_gene * self.number_of_genes,
                                                       self.k_intra + self.k_jump) 

    def 
