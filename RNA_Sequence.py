"""
This module should provide a foundation to use viennaRNA
sequences
"""
import mixins
import random

random_generator = random.Random()


class RNAsequence(mixins.KeyedComparisonMixin, mixins.KeyedHashingMixin):
    def __init__(self, value):
        self.value = [base for base in value]

    def __len__(self):
        return len(self.value)

    def __key__(self):
        return self.value

    def __getitem__(self, key):
        return self.value[key]

    def __setitem__(self, key, item):
        self.value[key] = item

    def __iter__(self):
        return iter(self.value)

def change_base(RNA, position):
    value = list(RNA)
    possibilities = ['g', 'c', 'a', 'u']
    for pos in position:
        mutate_to = random_generator.choice(possibilities)
        while value[pos] == mutate_to:
            mutate_to = random_generator.choice(possibilities)
        value[pos] = mutate_to
    return RNAsequence(value)
