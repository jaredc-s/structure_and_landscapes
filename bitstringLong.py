"""
Module implements Bitstring as a long int and mutates as
an XOR comparison
"""
import mixins


class Bitstring(mixins.KeyedComparisonMixin, mixins.KeyedHashingMixin):

    def __init__(self, iterable):
        self.value = long(iterable, 2)

    def __str__(self):
        return bin(self.value)[2:]

    def __len__(self):
        return len(bin(self.value)) - 2

    def __getitem__(self, key):
        return bin(self.value)[key + 2]

    def __iter__(self):
        return iter(bin(self.value)[2:])

    def __key__(self):
        return self.value

    def __int__(self):
        return self.value


def flip_positions(bitstring_instance, positions_to_flip):
    int_value = bitstring_instance.value
    for pos in positions_to_flip:
        int_value = (int_value ^ (2 ** pos))
    bin_value = bin(int_value)[2:]
    return Bitstring(bin_value)
