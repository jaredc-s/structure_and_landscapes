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


def run_struc(struc_pop):
    fit_list = []
    for gen in range(updates):
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




fp = open("parameters.cfg")
fp.readline()
fp.readline()
fp.readline()
fp.readline()
mut_rate = float(fp.readline().split(":")[1].strip())
num_org = int(fp.readline().split(":")[1].strip())
pops = int(fp.readline().split(":")[1].strip())
mig_rate = float(fp.readline().split(":")[1].strip())
swap_rate = float(fp.readline().split(":")[1].strip())
org_type = fp.readline().split(":")[1].strip()
len_org = int(fp.readline().split(":")[1].strip())
len_gene = int(fp.readline().split(":")[1].strip())
num_gene = int(fp.readline().split(":")[1].strip())
k_tot = int(fp.readline().split(":")[1].strip())
k_intra = int(fp.readline().split(":")[1].strip())
updates = int(fp.readline().split(":")[1].strip())

random.seed(1)

if org_type == "RNA":
    if pops <= 1:
        swap_rate = 0
        mig_rate = 0
    org = rna_organism.random_organism()
    org_list = [org for _ in range(num_org)]
    pop_list = [Population(org_list) for _ in range(pops)]
    structured_pop = Structured_Population(pop_list,
                                           migration_rate=mig_rate,
                                           proportion_of_pop_swapped=swap_rate)
    run_struc(structured_pop)

elif org_type == "Bitstring":
    pass
elif org_type == "NK Model":
    if pops <= 1:
        mig_rate = 0
        swap_rate = 0
    b = bs.bitstring.random_string(len_org)
    nk_fac = bs.nk_model.NKModelFactory()
    nk_org = bs.nk_organism.Organism(
        b, nk_fac.consecutive_dependencies_multigene(
                n_per_gene=len_gene, number_of_genes=num_gene, k_intra_gene=k_intra, k_total=k_tot))
    org_list = [nk_org for _ in range(num_org)]
    pop_list = [Population(org_list, mut_rate) for _ in range(pops)]
    structured_pop = Structured_Population(pop_list, 
                                           migration_rate=mig_rate,
                                           proportion_of_pop_swapped=swap_rate)
    run_struc(structured_pop)


else:
    raise TypeError("Not a valid org type")

