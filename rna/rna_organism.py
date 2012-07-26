"""
Organism where the genome is represented by RNA
"""
from structure_and_landscapes.utility import mixins as mixins
from structure_and_landscapes.rna import vienna_distance
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
        self._fitness = None

    def __key__(self):
        return self.value

    def __getitem__(self, key):
        return self.value[key]

    def mutate(self):
        """
        returns a new rna organism except
        its a different base at one position.
        """
        possibilities = ['G', 'C', 'A', 'T']
        sequence = self.value
        position = random.randrange(len(sequence))
        possibilities.remove(sequence[position])
        mutate_to = random.choice(possibilities)
        new_seq = sequence[:position] + mutate_to + sequence[position + 1:]
        return Organism(new_seq)

    def change_base(self, position):
        """
        Permutates a base at a given index. Returns a list of tuples
        where each tuple is a rna organism's sequence and fitness.
        """
        possibilites = ['G', 'C', 'A', 'T']
        sequence = self.value
        possibilites.remove(sequence[position])
        permutation_orgs = []
        for base in possibilites:
            new_seq = sequence[:position] + base + sequence[position + 1:]
            mutated_org = Organism(new_seq)
            permutation_orgs.append(mutated_org)

        return permutation_orgs

    @property
    def fitness(self):
        """
        This is where calls to vienna RNA will have to come in folding it to
        a predefined structure or seeing it's distance from tRNA
        """
        if self._fitness is None:
            num_diffs = vienna_distance.get_distance_from_tRNA_sequence(self.value)
            normalized_fitness = 2**(len(self.value) - num_diffs)
            self._fitness = (normalized_fitness)
        return self._fitness

    def __repr__(self):
        return "Organism('{}')".format(self.value)

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
