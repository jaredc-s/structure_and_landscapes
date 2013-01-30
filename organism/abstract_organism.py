"""
Generic organism class for inheritance.

Immutable class. Hashable. Equalible. Printable.
"""
from structure_and_landscapes.utility import mixins
import uuid
from abc import ABCMeta, abstractmethod


class AbstractOrganism(mixins.KeyedHashingMixin):
    __metaclass__ = ABCMeta

    def __init__(self, value, *args, **kwargs):
        """
        The value argument is the state that is used for evaluating fitness
        parent_id is a uuid marking the parent (for inheritance tracking)
        id is the self marker (passed to offspring)
        """
        self.value = value
        self._fitness = None
        for attr, set_value in kwargs.items():
            setattr(self, attr, set_value)
        if not hasattr(self, "parent_id"):
            self.parent_id = None
        if args:
            raise ValueError("Organisms can only take the value an unnamed argument")
        if not hasattr(self, "self_id") or self.self_id is None:
            self.self_id = uuid.uuid4()


    @abstractmethod
    def _mutated_value(self): # pragma: no cover
        """
        Concrete subclasses should override this.

        Should return a different, mutated value.
        note: original organism is unchanged
        """
        pass

    def mutate(self):
        return type(self)(
            value=self._mutated_value(),
            parent_id=self.self_id)

    @abstractmethod
    def _evaluate_fitness(self): # pragma: no cover
        """
        Method should return a float representing the fitness of the organism.

        Note the fitness for all possible organisms should be positive,
        non-zero floats (or integers).
        """
        pass

    @property
    def fitness(self):
        """
        fitness is the property that enquiring objects should query
        It implements a very simple form of caching.
        """
        if self._fitness is None:
            self._fitness = self._evaluate_fitness()
        return self._fitness

    def __key__(self):
        """
        Returns an object capable of being hashed and equaled
        """
        return self.value

    def __repr__(self):
        """
        Returns a repr string for the instantiation

        Example:
        Organism(value=Bitstring('10101'))
        """
        return "{}(value={!r}, self_id={!r}, parent_id={!r})".format(
            self.__class__.__name__,
            self.value,
            self.self_id,
            self.parent_id)
