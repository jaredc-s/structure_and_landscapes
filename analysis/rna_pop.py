from structure_and_landscapes.rna import rna_organism
from structure_and_landscapes.population import population, structure_population


def rna_org_structured_pop_demo():
    org = rna_organism.random_organism()
    org_list = [org for _ in range(1000)]
    pop_list = [population.Population(org_list, mutation_rate = 0.01) for _ in range(10)]
    structured_pop = structure_population.Structured_Population(pop_list,
                                                                migration_rate=0.2,
                                                                proportion_of_pop_swapped=0.05)
    run_struc(structured_pop)

def run_struc(struct_pop):
    fit_list = []
    for gen in range(150):
        print "["
        #for pop in struct_pop:

        struct_pop.advance_generation()
        print "]", gen
    
    print(fit_list[::10])
    
rna_org_structured_pop_demo()
