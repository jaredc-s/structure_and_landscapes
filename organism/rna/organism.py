"""
Organism where the genome is represented by RNA
"""
import random
import vienna_distance
from ..abstract_organism import AbstractOrganism

OPTIMAL_RNA_SEQUENCE = vienna_distance.get_tRNA_sequence()
RNA_SEQUENCE_LENGTH = len(OPTIMAL_RNA_SEQUENCE)


class Organism(AbstractOrganism):

    def __init__(self, *args, **kwargs):
        super(Organism, self).__init__(*args, **kwargs)
        if set(self.value) - set("ATUCG"):
            raise ValueError("RNA org only takes nucleotides (ATUCG)")

    def _mutated_value(self):
        """
        returns a new rna except
        it is a different base at one position.
        """
        possibilities = ['G', 'C', 'A', 'T']
        sequence = self.value
        position = random.randrange(len(sequence))
        possibilities.remove(sequence[position])
        mutate_to = random.choice(possibilities)
        return sequence[:position] + mutate_to + sequence[position + 1:]

    def _evaluate_fitness(self):
        """
        This is where calls to vienna RNA will have to come in folding it to
        a predefined structure or seeing it's distance from tRNA
        """
        num_diffs = vienna_distance.get_distance_from_tRNA_sequence(
            self.value)
        a = 0.01
        return 1 / (a + (float(num_diffs) / len(self.value)))


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
