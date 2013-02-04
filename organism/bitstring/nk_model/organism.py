from structure_and_landscapes.utility import mixins
from ..organism import Organism as BOrg
from .. import organism as bitstring_organism
from nk_model import NKModelSimple


class Organism(BOrg):
    def __init__(self, *args, **kwargs):
        super(Organism, self).__init__(*args, **kwargs)
        if (not hasattr(self, "nk_model") or
                not isinstance(self.nk_model, NKModelSimple)):
            raise ValueError("NK Organisms need a nk_model")

    def mutate(self):
        return type(self)(
            value=self._mutated_value(),
            parent_id=self.self_id,
            nk_model=self.nk_model)

    def _evaluate_fitness(self):
        return self.nk_model.calculate_fitness(self.value)
