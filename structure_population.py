import random
from selection import select
from population import Population

class Structured_Population(object):
    def __init__(self, sub_populations):
        self.all_pop = list(sub_population)
        
    def migrate(self,rate):
        """should happen after replicate but before the culling"""
        from_pop = self.all_pop[random.randint(0,len(self.pop) - 1)]
        from_org = from_pop[random.randint(0,len(from_pop))]

        to_pop = self.all_pop[random.randint(0,len(self.pop) - 1)]
        
        if to_pop.is_full():
            to_org = to_pop[random.randint(0,len(to_pop))]
            self.pop[to_pop][to_org] = self.pop[from_pop][from_org]
        else:
            to_pop.add_to_pop(from_org)

        from_pop.remove_from_pop(from_org)
            
