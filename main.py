from bitstring.bitstring_organism import Organism as bit_organism
from integer.integer_organism import Organism as int_organism
from bitstring.bitstring import Bitstring
from population.population import Population
from population.structure_population import Structured_Population
import bitstring.nk_model as nk_model
import bitstring as bs
import bitstring.nk_organism
import rna.rna_organism as rna_organism
from rna import vienna_distance

import numpy as np
import scipy.stats as st
import matplotlib.pyplot as plt

def int_org_demo():
    org_list = [int_organism(i) for i in range(1, 11)]
    pop = Population(org_list)
    run(pop)


def nk_org_demo():
    b = Bitstring("11010")
    nk_fac = bs.nk_model.NKModelFactory()
    nk_org = bs.nk_organism.Organism(
        b, nk_fac.consecutive_dependencies(n=5, k=2))
    org_list = [nk_org for _ in range(1, 5)]
    pop = Population(org_list)
    run(pop)


def nk_gene_demo():
    b = Bitstring("111000111")
    nk_fac = bs.nk_model.NKModelFactory()
    nk_org = bs.nk_organism.Organism(
        b, nk_fac.consecutive_dependencies_multigene(
            n_per_gene=3, number_of_genes=3, k_intra_gene=1, k_total=2))
    org_list = [nk_org for _ in range(10)]
    pop = Population(org_list)
    run(pop)


def nk_gene_structured_pop_demo():
    b = Bitstring("111000111")
    nk_fac = bs.nk_model.NKModelFactory()
    nk_org = bs.nk_organism.Organism(
        b, nk_fac.consecutive_dependencies_multigene(
            n_per_gene=3, number_of_genes=3, k_intra_gene=1, k_total=2))
    org_list = [nk_org for _ in range(10)]
    pop_list = [Population(org_list) for _ in range(10)]
    structured_pop = Structured_Population(pop_list, migration_rate=0.5,
                                           proportion_of_pop_swapped=0.5)
    run(structured_pop)


def bit_org_demo():
    base_bit = '0000000000'
    bit_list = [bit_organism(Bitstring(base_bit + '1' * i)) for i in range(10)]
    pop = Population(bit_list)
    run(pop)


def rna_org_demo():
    target = rna_organism.default_organism
    start_genome = "".join(["A" for _ in target.value])
    starting_org = rna_organism.Organism(start_genome)
    pop = Population([rna_organism.random_organism() for _ in range(100)], mutation_rate=.001)
    run(pop)


def rna_org_structured_pop_demo():
    org = rna_organism.random_organism()
    org_list = [org for _ in range(20)]
    pop_list = [Population(org_list) for _ in range(5)]
    structured_pop = Structured_Population(pop_list, migration_rate=0.5,
                                           proportion_of_pop_swapped=0.5)
    run_struc(structured_pop)


def structured_pop_demo():
    b = Bitstring("10011")
    org_list = [bit_organism(b) for i in range(1, 50)]
    pop_list = [Population(org_list) for _ in range(10)]
    struct_pop = Structured_Population(pop_list, migration_rate=0.5,
                                       proportion_of_pop_swapped=0.5)
    run_struc(struct_pop)


def average_fitness_of_structured_population(structured_population):
    """
    This functions computes the average fitness of
    all of the orgnisms residing in structured population!
    """
    list_of_fitnesses = [org.fitness for pop in
                         structured_population for org in pop]
    return sum(list_of_fitnesses) / float(len(list_of_fitnesses))


def run_struc(struc_pop):
    fit_list = []
    for gen in range(500):
        one_gen = [org.fitness for pop in struc_pop for org in pop]
        fit_list.append(one_gen)
        pop.advance_generation()

        print_best_structure(pop)
    #print(fit_list)
    print np.mean(fit_list[0]), st.sem(fit_list[0])
    print np.mean(fit_list[-1]), st.sem(fit_list[-1])

def print_best_structure(pop):
    fit_list = [(org.fitness, org) for org in pop]
    best_org =  max(fit_list)[1]
    print vienna_distance.fold(rna_organism.OPTIMAL_RNA_SEQUENCE)+'*'
    print vienna_distance.fold(best_org.value), best_org.fitness

def run(pop):
    for gen in range(500):
        pop.advance_generation()


if __name__=='__main__':
    nk_gene_structured_pop_demo()
    #rna_org_demo()
    #int_org_demo()
    #rna_org_structured_pop_demo()
