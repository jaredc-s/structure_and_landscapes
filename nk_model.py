"""
Implementation of Stuart Kauffman's NK Model.

Genomes are bitstrings of length "n".
The number of epistatic neighbors of a loci is denoted "k".

When k = 0, the adaptive landscape is smooth.
When k = n - 1, the landscape is maximally rugged.

Every locus in the bitstring has a respective function requiring
the state of the locus and its "k" neighbors (those immediately
following with wrapping about ends).

The outcome of each function is drawn from a  uniformly
distribution. The mean contribution of each locus is the fitness.
"""
import collections
import itertools
from random import Random
from bitstring import Bitstring
module_random_generator = Random()


class NKModelFactory(object):
    """
    Returns instances of NK models.
    """
    def __init__(self, random_generator=module_random_generator):
        self.random_generator = random_generator

    def no_dependancies(self, n):
        """
        Returns models of size n with k=0 (no epistatic dependancies)
        """
        deps = self._consecutive_dependancy_lists(n, 0)
        return self._model_with_uniform_contribution_lookup_table(deps)

    def max_dependancies(self, n):
        """
        Returns models of size n with the maximum amount of dependances
        k = (n - 1)
        """
        deps = self._consecutive_dependancy_lists(n, n - 1)
        return self._model_with_uniform_contribution_lookup_table(deps)

    def consecutive_dependancies(self, n, k):
        """
        Returns a model with the dependancies of a locus being the locus
        itself and the next k consecutive loci (with overflow/wrapping).
        """
        deps = self._consecutive_dependancy_lists(n, k)
        return self._model_with_uniform_contribution_lookup_table(deps)

    def _consecutive_dependancy_lists(self, n, k):
        """
        Returns a depandancy list for a given n and k, where dependancies
        are consecutive.
        """
        assert(k < n)
        loci = collections.deque(range(n))
        deps = []
        for _ in range(n):
            deps.append(list(itertools.islice(loci, 0, k + 1)))
            loci.rotate(-1)
        return deps

    def _non_consecutive_dependancy_lists(self, n, k):
        """
        Returns dependacy lists where the each locus's k dependacies are
        determined by random sampling (without replacement).
        """
        assert(k < n)
        deps = []
        for locus in range(n):
            chosen = [locus]
            potential_dependacies = list(range(n))
            potential_dependacies.remove(locus)
            chosen.extend(self.random_generator.sample(
                potential_dependacies, k))
            deps.append(chosen)
        return deps

    def non_consecutive_dependancies(self, n, k):
        deps = self._non_consecutive_dependancy_lists(n, k)
        return self._model_with_uniform_contribution_lookup_table(deps)

    def consecutive_dependancies_multigene(self, n_per_gene, number_of_genes,
        k_intra_gene, k_inter_gene):
        """
        Returns a multigene model with regular dependancies
        n_per_gene = the number of loci per gene
        number_of_genes = the number of subdivisions of the bitstring genome
        k_intra_gene = the number of dependancies within a gene per loci
        k_inter_gene = the number of dependancies between genes per loci, the
            dependancies will have the same index as the locus, but on
            consecutive genes
        """
        assert(k_intra_gene < n_per_gene)
        assert(k_inter_gene < number_of_genes)
        intra_deps = self._consecutive_dependancy_lists(
            n_per_gene, k_intra_gene)
        inter_deps = self._consecutive_dependancy_lists(
            number_of_genes, k_inter_gene)

        deps = []
        for gene in range(number_of_genes):
            offset = gene * n_per_gene
            gene_inter_deps = inter_deps[gene]
            for intra_locus in range(n_per_gene):
                loci_intra_deps = intra_deps[intra_locus]
                loci_deps = [locus + offset for locus in loci_intra_deps]
                loci_inter_deps = [(gene * n_per_gene) + intra_locus
                    for gene in gene_inter_deps]
                loci_deps.extend(loci_inter_deps[1:]) # don't double count locus
                deps.append(loci_deps)
        return self._model_with_uniform_contribution_lookup_table(deps)

    def non_consecutive_dependancies_multigene(self, n_per_gene, number_of_genes,
        k_intra_gene, k_total):
        """
        Returns a multigene model with regular dependancies
        n_per_gene = the number of loci per gene
        number_of_genes = the number of subdivisions of the bitstring genome
        k_intra_gene = the number of dependancies within a gene per loci
        k_total = the number of total dependancies, the not k_intra
            dependancies are uniformly drawn from all not-already-included-loci
        """
        assert(k_intra_gene < n_per_gene)
        assert(k_total < (n_per_gene * number_of_genes))

        deps = []
        for gene in range(number_of_genes):
            offset = gene * n_per_gene
            gene_intra_deps = self._non_consecutive_dependancy_lists(n_per_gene, k_intra_gene)
            for intra_locus in range(n_per_gene):
                loci_intra_deps = gene_intra_deps[intra_locus]
                loci_deps = [locus + offset for locus in loci_intra_deps]
                all_loci = set(range(n_per_gene * number_of_genes))
                potential_deps = all_loci - set(loci_deps)
                while len(loci_deps) < k_total + 1:
                    chosen = self.random_generator.choice(list(potential_deps))
                    loci_deps.append(chosen)
                    potential_deps.remove(chosen)
                deps.append(loci_deps)
        return self._model_with_uniform_contribution_lookup_table(deps)

    def _model_with_uniform_contribution_lookup_table(self, dependancy_lists):
        """
        Fitness is the mean of the contribution of each loci.
        Each loci has its own lookup table composed of 2 ** (number of dependancies)
        uniformly distributed entries corresponding to the numerical value of the
        subbitstring (locus + k neighbors).
        """
        clt = [[self.random_generator.random() for _ in range(2 ** len(dep_list))]
            for dep_list in dependancy_lists]
        return NKModelSimple(dependancy_lists, clt)


class NKModelSimple(object):
    def __init__(self, dependancy_lists,
                 contribution_lookup_tables):
        """
        The nk model has the dependancy_lists (for each loci, and ordered
        list of loci needed to determine the fitness contribution) and a
        contribution_lookup_tables (for each loci, the fitness
        contribution of each possible genotype string).
        """
        self.dependancy_lists = dependancy_lists
        self.contribution_lookup_tables = contribution_lookup_tables

    def calculate_fitness(self, bitstring):
        """
        Returns the fitness of a bitstring by tallying the
        contributions of each loci.
        """
        num_loci = len(bitstring)
        assert(num_loci <= len(self.dependancy_lists) and
            num_loci <= len(self.contribution_lookup_tables))
        fitness_tally = 0.0
        for loci in range(num_loci):
            dependancy_list = self.dependancy_lists[loci]
            contribution_index = bitstring.selected_loci_as_int(
                dependancy_list)
            lookup_table = self.contribution_lookup_tables[loci]
            fitness_tally += lookup_table[contribution_index]
        return fitness_tally / num_loci
