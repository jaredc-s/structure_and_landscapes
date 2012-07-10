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
        the iterable will be converted to a tuple (reversed so that the 0'th
        is first). Otherwise, the iterable is converted to a list of booleans.

        for example:
             "10010" --> (False, True, False, False, True)
            [0, None, [], 'hello', 10] --> (False, False, False, Truei, True)
        """

        if isinstance(iterable, str):
            self._value = tuple(char == "1" for char in reversed(iterable))
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

        value_as_string = "".join(bool_to_str(pos) for pos in reversed(self))
        return "{}({!r})".format(self.__class__.__name__, value_as_string)

    def __int__(self):
        return sum(2 ** i for i, value in enumerate(self) if value)

    def hamming_distance(self, other):
        """
        This returns the number of differences between two bitstrings
        note bitstrings must be the same length
        if different lengths only compare to the length of the shorter
        """
        return len(tuple(None for (self_pos, other_pos) in zip(
            self, other) if self_pos != other_pos))

    def selected_loci_as_int(self, loci):
        """
        Coverts an iterable (loci) into an integer representing the state of
        the bitstring at those positions.
        """
        tally = 0
        for i, locus in enumerate(loci):
            if self[locus]:
                tally += (2 ** i)
        return tally


def flip_position(bitstring_instance, position_to_flip):
    """
    Function takes a bitstring and an index to
    flip (True --> False), (False-->True)
    returns a new bitstring with the modification
    """
    values = list(bitstring_instance)
    values[position_to_flip] = not values[position_to_flip]
    return Bitstring(values)
