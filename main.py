from bitstring_organism import Organism as bit_organism
from integer_organism import Organism as int_organism
from bitstring import Bitstring
import mutate
import population
from population import Population
from basic_plot import *
from structure_population import Structured_Population


def int_org_demo():
    org_list = [int_organism(i) for i in range(1, 11)]

    pop = Population(org_list, 100)
    run(pop)

def bit_org_demo():
    base_bit = '0000000000'
    bit_list = [bit_organism(Bitstring(base_bit + '1' * i)) for i in range(10)]

    pop = Population(bit_list, 100)
    run(pop)

def structured_pop_demo():
    org_list = [int_organism(i) for i in range(1, 11)]
    pop_list = [Population(org_list) for _ in range(10)]
    struct_pop = Structured_Population(pop_list, 0.5, 0.5)
    
    for _ in range(50):
        population_state(struct_pop)
        struct_pop.advance_generation()

def population_state(struct_pop):
    for subpop in struct_pop:
        print "[",
        for org in subpop:
            print org.fitness,
        print "]"
    print "\n"


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
    #bit_org_demo()
    #int_org_demo()
    structured_pop_demo()

if __name__ == "__main__":
    main()
