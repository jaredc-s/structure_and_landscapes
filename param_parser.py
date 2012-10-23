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

import random
import numpy as np
import scipy.stats as st
import matplotlib.pyplot as plt


def run_struc(struc_pop, number_of_generations):
    fit_list = []
    for gen in range(number_of_generations):
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
    print best_org
    #print vienna_distance.fold(rna_organism.OPTIMAL_RNA_SEQUENCE)+'*'
    #print vienna_distance.fold(best_org.value), best_org.fitness

class OrgException(Exception):
    pass

random.seed(1)

parameter_settings = {}
with open("parameters.cfg") as parameters_file:
    for line in parameters_file:
        line_without_comments, _, _ = line.partition("#")
        line_stripped = line_without_comments.strip()
        if not line_stripped:
            continue
        parameter, _, value = line_stripped.partition(":")
        parameter_settings[parameter] = value

print(parameter_settings)

if parameter_settings["Organism Type"] == "RNA":
    org = rna_organism.random_organism()
elif parameter_settings["Organism Type"] == "Bitstring":
    pass
elif parameter_settings["Organism Type"] == "NK Model":
    b = bs.bitstring.random_string(int(parameter_settings["Length of Org"]))
    nk_fac = bs.nk_model.NKModelFactory()
    length_of_gene = int(parameter_settings["Length of Gene"])
    number_of_genes = int(parameter_settings["Number of Genes"])
    k_intra = int(parameter_settings["K-intra"])
    k_total = int(parameter_settings["K-total"])

    nk_model =  nk_fac.consecutive_dependencies_multigene(
            n_per_gene=length_of_gene,
            number_of_genes=number_of_genes,
            k_intra_gene=k_intra,
            k_total=k_total)
    org = bs.nk_organism.Organism(
            b, nk_model)
else:
    raise OrgException("Not a valid org type")



number_of_pops = int(parameter_settings["Number of Populations"])
if number_of_pops <= 1:
    mig_rate = 0.0
    swap_rate = 0.0
else:
    mig_rate = float(parameter_settings["Migration Rate"])
    swap_rate = float(parameter_settings["Proportion of Population Migrated"])

orgs_per_population = int(parameter_settings["Orgs per Population"])


org_list = [org for _ in range(orgs_per_population)]
pop_list = [Population(org_list) for _ in range(number_of_pops)]
structured_pop = Structured_Population(
        pop_list,
        migration_rate=mig_rate,
        proportion_of_pop_swapped=swap_rate)
run_struc(structured_pop, int(parameter_settings["Number of Generations"]))




