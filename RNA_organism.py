"""
Organism where the genome is represented by RNA
"""
import mixins
import mutate

class Organism(mixins.KeyedHashingMixin):
    def __init__(self, value):
        """
        The genome of a RNA Organism is a string of letters
        composed of "AGCU".
        """
        self.value = value

    def __key__(self):
        return self.value

    def __getitem__(self,key):
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
        pass
