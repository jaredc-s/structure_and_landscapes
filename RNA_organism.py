"""
Organism where the genome is represented by RNA
"""
import mixins
import RNA_Sequence as RS

class Organism(mixins.KeyedHashingMixin):
    def __init__(self, value):
        self.value = RS.RNAsequence(value)
        #consider making this self.value =RS.RNA_sequence(value)
        #that would tie them together better
        #Do for every org type

    def __key__(self):
        return self.value

    def mutate(self):
        return Organism(self._mutate_value())

    def _mutate_value(self):
        return muatate_value(self.value)

    @property
    def fitness(self):
        """
        This is where calls to vienna RNA will have to come in folding it to 
        a predefined structure or seeing it's distance from tRNA
        """
        pass
