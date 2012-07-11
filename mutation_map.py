import bitstring_organism
import bitstring
#import integer_organism
import nk_organism
#import rna_organism
import nk_model

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
        print count
        if organism.fitness < max(bitstring_org_mutation_map):
            organism = bitstring_org_mutation_map[max(bitstring_org_mutation_map)]
        else:
            break
    return bitstring_org_mutation_map, organism.fitness

nk = nk_model.NKModelFactory()
simple_nk = nk.non_consecutive_dependencies_multigene(5, 2, 3, 5)
init_bitstring = bitstring.Bitstring('1011001101')
bitstring_org = nk_organism.Organism(init_bitstring, simple_nk)
print nk_org_mutation_map(bitstring_org, simple_nk)
