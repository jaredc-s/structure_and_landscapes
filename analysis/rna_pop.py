from structure_and_landscapes.rna import rna_organism
from structure_and_landscapes.population import population, structure_population


def rna_org_structured_pop_demo():
    org = rna_organism.random_organism()
    org_list = [org for _ in range(1000)]
    pop_list = [population.Population(org_list, mutation_rate = 0.1) for _ in range(10)]
    structured_pop = structure_population.Structured_Population(pop_list,
                                                                migration_rate=0.2,
                                                                proportion_of_pop_swapped=0.1)
    run_struc(structured_pop)

def run_struc(struc_pop):
    fit_list = []
    for gen in range(250):
        one_gen = [org.fitness for pop in struc_pop for org in pop]
        fit_list.append(sum(one_gen)/1000.0)
        pop.advance_generation()
    print(fit_list)

rna_org_structured_pop_demo()
