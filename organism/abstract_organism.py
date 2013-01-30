"""
Generic organism class for inheritance.

Immutable class. Hashable. Equalible. Printable.
"""
from structure_and_landscapes.utility import mixins
import uuid
import abc


class AbstractOrganism(mixins.KeyedHashingMixin):
    __metaclass__ = abc.ABCMeta

    def __init__(self, value, parent_id=None, self_id=None):
        """
        The value argument is the state that is used for evaluating fitness
        parent_id is a uuid marking the parent (for inheritance tracking)
        id is the self marker (passed to offspring)
        """
        self.value = value
        self._fitness = None
        self.parent_id = parent_id
        if self_id is None:
            self.self_id = uuid.uuid4()

    @abc.abstractmethod
    def _mutated_value(self):
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

    @abc.abstractmethod
    def _evaluate_fitness(self):
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
