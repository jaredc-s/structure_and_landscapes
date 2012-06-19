from bitstring_organism import Organism as bit_organism
from integer_organism import Organism as int_organism
from bitstring import Bitstring
import mutate
import population
from population import Population
from basic_plot import *


def int_org_demo():
    org_list = [int_organism(i) for i in range(1, 11)]

    pop = Population(org_list, 100)
    run(pop)

def bit_org_demo():
    base_bit = '0000000000'
    bit_list = [bit_organism(Bitstring(base_bit + '1' * i)) for i in range(10)]

    pop = Population(bit_list, 100)
    run(pop)

def run(pop):
    fit_list = []
    for gen in range(51):
        one_gen = []
        for org in pop:
            print org.fitness,
            one_gen.append(org.fitness)
        fit_list.append(one_gen)
        print'\n'
        pop.advance_generation()
    plot_average_fitness(fit_list)


def main():
    bit_org_demo()
    int_org_demo()

if __name__ == "__main__":
    main()
