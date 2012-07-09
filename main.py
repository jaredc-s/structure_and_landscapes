from bitstring_organism import Organism as bit_organism
from integer_organism import Organism as int_organism
from bitstring import Bitstring
import mutate
import population
from population import Population
from basic_plot import average
from structure_population import Structured_Population
import nk_organism
from nk_organism import Organism as nk_org
import nk_model
import nk_model_with_genes
import rna_organism


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


def nk_gene_demo():
    b = Bitstring("0100000001010101101010100111")
    nk = nk_model_with_genes.NKWithGenes(3, 1, 7, 4)
    org_list = [nk_org(b, nk) for _ in range(10)]
    pop = Population(org_list)
    run(pop)


def nk_gene_structured_pop_demo():
    b = Bitstring("0100000001010101101010100111")
    nk = nk_model_with_genes.NKWithGenes(3, 1, 7, 4)
    org_list = [nk_org(b, nk) for _ in range(10)]
    pop_list = [Population(org_list) for _ in range(10)]
    structured_pop = Structured_Population(pop_list, migration_rate=0.5,
                                           proportion_of_pop_swapped=0.5)

    avg_fit_pop = [zeros(50) for _ in range(len(pop_list))]

    for i in range(50):
        avg_fit_pop = population_state(structured_pop, avg_fit_pop, i)
        structured_pop.advance_generation()


def bit_org_demo():
    base_bit = '0000000000'
    bit_list = [bit_organism(Bitstring(base_bit + '1' * i)) for i in range(10)]

    pop = Population(bit_list, 100)
    run(pop)


def rna_org_demo():
    target = rna_organism.default_organism
    start_genome = "".join(["A" for _ in target.value])
    starting_org = rna_organism.Organism(start_genome)
    print starting_org.fitness


def rna_org_structured_pop_demo():
    org = rna_organism.default_organism
    #use string random generator method in rna_org
    org_list = [org for _ in range(10)]
    pop_list = [Population(org_list) for _ in range(10)]
    structured_pop = Structured_Population(pop_list, migration_rate=0.5,
                                           proportion_of_pop_swapped=0.5)

    print average_fitness_of_structured_population(structured_pop)


def structured_pop_demo():
    b = Bitstring("10011")
    org_list = [bit_organism(b) for i in range(1, 50)]
    pop_list = [Population(org_list) for _ in range(10)]
    struct_pop = Structured_Population(pop_list, migration_rate=0.5,
                                       proportion_of_pop_swapped=0.5)

    avg_fit_pop = [zeros(50) for _ in range(len(pop_list))]

    for i in range(50):
        #avg_fit_pop = population_state(struct_pop, avg_fit_pop, i)
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
        print "[",
        for org in subpop:
            print org.fitness,
            dummy.append(org.fitness)
        fit_holder[i][gen_number] = average(dummy)
        print "]"
    print "\n"
    return fit_holder


def average_fitness_of_structured_population(structured_population):
    """
    This functions computes the average fitness of
    all of the orgnisms residing in structured population!
    """
    list_of_fitnesses = [org.fitness for pop in
                         structured_population for org in pop]
    return average(list_of_fitnesses)


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
    #nk_org_demo()
    #nk_gene_demo()
    #nk_gene_structured_pop_demo()
    #rna_org_demo()
    rna_org_structured_pop_demo()


if __name__ == "__main__":
    main()
