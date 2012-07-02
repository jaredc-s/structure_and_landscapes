from bitstring_organism import Organism as bit_organism
from integer_organism import Organism as int_organism
from bitstring import Bitstring
import mutate
import population
from population import Population
from basic_plot import *
from structure_population import Structured_Population
import nk_organism
from nk_organism import Organism as nk_org
import nk_model

def int_org_demo():
    org_list = [int_organism(i) for i in range(1, 11)]

    pop = Population(org_list, 100)
    run(pop)

def nk_org_demo():
    b = Bitstring("11010")
    nk = nk_model.NKModel(n=5, k=2)
    org_list = [nk_org(b, nk) for _ in range(1, 5)]

    pop = Population(org_list)
    run(pop)


def bit_org_demo():
    base_bit = '0000000000'
    bit_list = [bit_organism(Bitstring(base_bit + '1' * i)) for i in range(10)]

    pop = Population(bit_list, 100)
    run(pop)


def structured_pop_demo():
    b = Bitstring("10011")
    org_list = [bit_organism(b) for i in range(1, 50)]
    pop_list = [Population(org_list) for _ in range(10)]
    struct_pop = Structured_Population(pop_list, migration_rate=0.5,
                                       proportion_of_pop_swapped=0.5)

    avg_fit_pop = [zeros(50) for _ in range(len(pop_list))]

    for i in range(50):
        avg_fit_pop = population_state(struct_pop, avg_fit_pop, i)
        struct_pop.advance_generation()

   # xlabel("Fitness")
   # ylabel("Updates")
   # pyplot.legend([str(i) for i in range(1, 10)], loc=2)
   # plot(transpose(avg_fit_pop))
   # show()


def population_state(struct_pop, fit_holder, gen_number):
    for i in range(len(struct_pop)):
        subpop = struct_pop[i]
        dummy = []
       # print "[",
        for org in subpop:
           # print org.fitness,
             dummy.append(org.fitness)
        fit_holder[i][gen_number] = average(dummy)
       # print "]"
   # print "\n"
    return fit_holder


def run(pop):
    fit_list = []
    for gen in range(50):
        one_gen = []
        for org in pop:
            print org.fitness,
            one_gen.append(org.fitness)
        fit_list.append(one_gen)
        print'\n'
        pop.advance_generation()
   # plot_average_fitness(fit_list)


def main():
    #bit_org_demo()
    #int_org_demo()
    #structured_pop_demo()
    nk_org_demo()
if __name__ == "__main__":
    main()
