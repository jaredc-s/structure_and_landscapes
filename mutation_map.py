import bitstring_organism
import bitstring
#import integer_organism
#import nk_organism
#import rna_organism


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

init_bitstring = bitstring.Bitstring('10110')
bitstring_org = bitstring_organism.Organism(init_bitstring)
print bitstring_organsism_mutation_map(bitstring_org)
