"""
This module implements a crude Bitstring with boolean values
in python tuples. Bitstring instances are immutable.
"""


class Bitstring(object):

    def __init__(self, iterable):
        if isinstance(iterable, str):
            self._value = tuple(char == "1" for char in iterable)
        else:
            self._value = tuple(bool(char) for char in iterable)

    def __len__(self):
        return len(self._value)

    def __getitem__(self, key):
        return self._value[key]

    def __iter__(self):
        return iter(self._value)

    def __hash__(self):
        return hash(self._value)

    def __eq__(self, other):
        if not isinstance(other, type(self)):
            return False
        return self._value == other._value

    def __ne__(self, other):
        return not self == other

    def __repr__(self):
        def bool_to_str(boolean):
            if boolean:
                return "1"
            return "0"

        value_as_string = "".join(
                bool_to_str(pos) for pos in self)
        return "{}({!r})".format(self.__class__.__name__, value_as_string)

    def hamming_distance(self, other):
        return len(tuple(None for (self_pos, other_pos)
                in zip(self, other) if self_pos != other_pos))


def flip_positions(bitstring_instance, positions_to_flip):
    values = list(bitstring_instance)
    for pos in positions_to_flip:
        values[pos] = not values[pos]
    return Bitstring(values)
