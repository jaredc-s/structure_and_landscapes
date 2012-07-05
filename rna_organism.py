"""
Organism where the genome is represented by RNA
"""
import mixins
import mutate
import vienna_distance
import random

OPTIMAL_RNA_SEQUENCE = vienna_distance.get_tRNA_sequence()
RNA_SEQUENCE_LENGTH = len(OPTIMAL_RNA_SEQUENCE)

class Organism(mixins.KeyedHashingMixin):
    def __init__(self, value):
        """
        The genome of a RNA Organism is a string of letters
        composed of "AGCU".
        """
        self.value = value

    def __key__(self):
        return self.value

    def __getitem__(self, key):
        return self.value[key]

    def mutate(self):
        new_seq = mutate.mutate_value(self.value)
        return Organism(new_seq)

    @property
    def fitness(self):
        """
        This is where calls to vienna RNA will have to come in folding it to
        a predefined structure or seeing it's distance from tRNA
        """
        num_diffs = vienna_distance.get_distance_from_tRNA_sequence(self.value)
        return (len(self.value) - num_diffs) / float(len(self.value))

default_organism = Organism(OPTIMAL_RNA_SEQUENCE)

def random_organism():
    """
    returns an rna organism with a randomly generated
    genome of the same length as our optimal rna sequence
    """
    nucleotides = ['A', 'T', 'G', 'C']
    sequence = [random.choice(nucleotides) for _ in range(RNA_SEQUENCE_LENGTH)]
    sequence_string = "".join(sequence)
    return Organism(sequence_string)


