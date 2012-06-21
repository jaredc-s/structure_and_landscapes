"""
This module implements a crude Bitstring with boolean values
in python tuples. Bitstring instances are immutable.
"""
import mixins


class Bitstring(mixins.KeyedComparisonMixin, mixins.KeyedHashingMixin):

    def __init__(self, iterable):
        """
        init takes a single argument

        If that argument is a string, where the string has a character of 1,
        the bit string will be true at that position.

        If the argument is not a string,
        the iterable will be converted to a tuple
        composed of booleans where each value is coerced to a boolean.

        for example:
             "1001" --> (True, False, False, True)
            [1, 0, None, [], 'hello'] --> (True, False, False, False, True)
        consider converting bitstring into long data type
        """

        if isinstance(iterable, str):
            self._value = tuple(char == "1" for char in iterable)
        else:
            self._value = tuple(bool(value) for value in iterable)

    def __len__(self):
        """
        length of a bitstring is the number of elements
        """
        return len(self._value)

    def __getitem__(self, key):
        """
        bitstrings can be accessed by index
        for example:
            Bitstring("101")[0] = True
            Bitstring("101")[1] = False
        """
        return self._value[key]

    def __iter__(self):
        """
        Bitstrings are iterable
        """
        return iter(self._value)

    def __key__(self):
        """
        Returns a key object that can be compared, hashed and equaled.
        """
        return tuple(self._value)

    def __repr__(self):
        """
        Bitstrings can be printed
        """
        def bool_to_str(boolean):
            """
            Helper Function converting a bool to the characters 1 or 0
            """
            if boolean:
                return "1"
            return "0"

        value_as_string = "".join(bool_to_str(pos) for pos in self)
        return "{}({!r})".format(self.__class__.__name__, value_as_string)

    def hamming_distance(self, other):
        """
        This returns the number of differences between two bitstrings
        note bitstrings must be the same length
        if different lengths only compare to the length of the shorter
        """
        return len(tuple(None for (self_pos, other_pos) in zip(
            self, other) if self_pos != other_pos))


def flip_positions(bitstring_instance, positions_to_flip):
    """
    Function takes a bitstring and a list of indicies to
    flip (True --> False), (False-->True)
    returns a new bitstring with the modification
    """
    values = list(bitstring_instance)
    for pos in positions_to_flip:
        values[pos] = not values[pos]
    return Bitstring(values)
