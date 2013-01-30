from structure_and_landscapes.utility import mixins
from ..organism import Organism as BOrg
from .. import organism as bitstring_organism
from nk_model import NKModelSimple


class Organism(BOrg):
    def __init__(self, *args, **kwargs):
        super(Organism, self).__init__(*args, **kwargs)
        if not hasattr(self, "nk_model") or not isinstance(self.nk_model, NKModelSimple):
            raise ValueError("NK Organisms need a nk_model")

    def _evaluate_fitness(self):
        return self.nk_model.calculate_fitness(self.value)
