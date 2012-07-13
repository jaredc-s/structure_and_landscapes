import random
from structure_and_landscapes.bitstring import bitstring_organism
from structure_and_landscapes.bitstring import bitstring
from structure_and_landscapes.bitstring import nk_organism
from structure_and_landscapes.bitstring import nk_model


#import integer_organism
#import nk_organism
#import rna_organism
#import nk_model


def bitstring_organism_mutation_map(organism):
    """
    mutates every possible single step mutation from a intial
    organism of the correct type passed in. Returns a
    list of tuples where each pair is a bitstring and its
    corresponding fitness.
    """
    bitstring_value = organism.value
    bitstring_org_mutation_map = []
    for i in range(len(bitstring_value)):
        perturbed_bitstring = bitstring.flip_position(bitstring_value, i)
        perturbed_organism = bitstring_organism.Organism(perturbed_bitstring)
        bitstring_org_mutation_map.append((perturbed_bitstring, perturbed_organism.fitness))

    return bitstring_org_mutation_map

#bit = bitstring.Bitstring('0000')
#bit_org = bitstring_organism.Organism(bit)
#print bitstring_organism_mutation_map(bit_org)

def nk_organism_mutation_map(organism, nk):
    bitstring_value = organism.value
    nk_organism_mutation_map = []
    for i in range(len(bitstring_value)):
        perturbed_bitstring = bitstring.flip_position(bitstring_value, i)
        perturbed_organism = nk_organism.Organism(perturbed_bitstring, nk)
        nk_organism_mutation_map.append((perturbed_bitstring, perturbed_organism.fitness))

    return nk_organism_mutation_map

#length_of_desired_genome = 16
#k_intra = 4
#k_total = 6
#bit = bin(random.getrandbits(length_of_desired_genome))[2:]
#bit = bit.rjust(length_of_desired_genome, '0')
#nk_model_type = nk_model.NKModelFactory()
#use_model = nk_model_type.non_consecutive_dependencies_multigene(8, 2, k_intra, k_total)
#nk_org = nk_organism.Organism(bitstring.Bitstring(bit), use_model)

#print nk_organism_mutation_map(nk_org, use_model)

def rna_organism_mutation_map(organism):
    rna_seq = organism.value
    rna_organism_mutation_map = []
    for i in range(len(ran_seq)):




