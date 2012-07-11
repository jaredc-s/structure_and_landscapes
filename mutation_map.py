import bitstring_organism
import bitstring
#import integer_organism
import nk_organism
#import rna_organism
import nk_model
import random
import population
import structure_population

def bitstring_organsism_mutation_map(organism):
    """
    mutates every possible single step mutation from a intial
    organism of the correct type passed in. Returns a
    dictionary of the fitness of the the orgs.
    """
    bitstring_org_mutation_map = {}
    bitstring_value = organism.value
    for i in range(len(bitstring_value)):
        perturbed_bitstring = bitstring.flip_position(bitstring_value, i)
        perturbed_organism = bitstring_organism.Organism(perturbed_bitstring)
        bitstring_org_mutation_map[perturbed_organism] = perturbed_organism.fitness

    return bitstring_org_mutation_map

def nk_org_mutation_map(organism, nk):
    count = 0
    while True:
        bitstring_org_mutation_map = {}
        bitstring_value = organism.value
        for i in range(len(bitstring_value)):
            perturbed_bitstring = bitstring.flip_position(bitstring_value, i)
            perturbed_organism = nk_organism.Organism(perturbed_bitstring, nk)
            bitstring_org_mutation_map[perturbed_organism.fitness] = perturbed_organism
        count += 1
        if organism.fitness < max(bitstring_org_mutation_map):
            organism = bitstring_org_mutation_map[max(bitstring_org_mutation_map)]
        else:
            break
    print count
    return organism.fitness

len_desired_genome = 16
k_intra = 4
k_total = 6
bit = bin(random.getrandbits(len_desired_genome))[2:]
bit = bit.rjust(len_desired_genome, '0')
nk = nk_model.NKModelFactory()
use_model = nk.non_consecutive_dependencies_multigene(8, 2, k_intra, k_total)

org = nk_organism.Organism(bitstring.Bitstring(bit), use_model)

pop = population.Population([org for _ in range(50)], 0.05)
struct = structure_population.Structured_Population([pop for _ in range(50)],
                                                    0.2, 0.1)

struct_avg = []
for gen in range(250):
    sum = 0
    struct_sum = 0
    #for org in only_pop:
    #    sum += org.fitness
    #avg.append(sum/500.0)
    for pop in struct:
        for org in pop:
            struct_sum += org.fitness
    struct_avg.append(struct_sum / 2500.0)
    struct.advance_generation()
    #only_pop.advance_generation()
    print "Gen: {}".format(gen)

print struct_avg[-1]
fin_dom_fit = 0
for i in range(1000):
    fin_dom_fit += nk_org_mutation_map(org, use_model)

print fin_dom_fit/1000.0


