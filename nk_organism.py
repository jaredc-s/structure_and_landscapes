import mixins
from bitstring_organism import Organism as BOrg
import bitstring_organism


class Organism(BOrg):
    def __init__(self, value, nk_model):
        self.nk_model = nk_model
        self.fit = None
        super(Organism, self).__init__(value)

    @property
    def fitness(self):
        if self.fit is None:
            self.fit = self.nk_model.determine_fitness(self.value)
        return self.fit

    def mutate(self, rate = 0.2):
        """
        the mutate method of an organism calls the module
        mutate and returns a new organism with the mutation
        note: original organism is unchanged
        """
        return Organism(self._mutate_value(rate), self.nk_model)
