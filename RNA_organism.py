"""
Organism where the genome is represented by RNA
"""
import mixins
import RNA_Sequence as RS
import mutate

class Organism(mixins.KeyedHashingMixin):
    def __init__(self, value):
        self.value = RS.RNAsequence(value)
        #consider making this self.value =RS.RNA_sequence(value)
        #that would tie them together better
        #Do for every org type

    def __key__(self):
        return self.value

    def __getitem__(self,key):
        return self.value[key]
    
    def mutate(self, rate = 0.2):
        return Organism(self._mutate_value(rate))

    def _mutate_value(self, rate):
        return mutate.mutate_value(self.value, rate)

    @property
    def fitness(self):
        """
        This is where calls to vienna RNA will have to come in folding it to 
        a predefined structure or seeing it's distance from tRNA
        """
        pass
