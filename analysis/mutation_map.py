import random
from structure_and_landscapes.bitstring import bitstring_organism
from structure_and_landscapes.bitstring import bitstring
from structure_and_landscapes.bitstring import nk_organism
from structure_and_landscapes.bitstring import nk_model
from structure_and_landscapes.rna import rna_organism

#import integer_organism
#import nk_organism
#import rna_organism
#import nk_model


def bitstring_organism_mutation_map(organism):
    """
    mutates every possible single step mutation from a intial
    organism of the correct type passed in. Returns a
    list of tuples where each pair is a bitstring_organism and its
    corresponding fitness.
    """
    bitstring_value = organism.value
    bitstring_org_mutation_map = []
    for i in range(len(bitstring_value)):
        perturbed_bitstring = bitstring.flip_position(bitstring_value, i)
        perturbed_organism = bitstring_organism.Organism(perturbed_bitstring)
        bitstring_org_mutation_map.append((
            perturbed_bitstring, perturbed_organism.fitness))
    return bitstring_org_mutation_map

#bit = bitstring.Bitstring('0000')
#bit_org = bitstring_organism.Organism(bit)
#print bitstring_organism_mutation_map(bit_org)


def nk_organism_mutation_map(organism, nk):
    """
    mutates every possible single step mutation from a intial
    organism of the correct type passed in. Returns a
    list of tuples where each tuple is a nk_organism and its
    corresponding fitness.
    """

    bitstring_value = organism.value
    nk_organism_mutation_map = []
    for i in range(len(bitstring_value)):
        perturbed_bitstring = bitstring.flip_position(bitstring_value, i)
        perturbed_organism = nk_organism.Organism(perturbed_bitstring, nk)
        nk_organism_mutation_map.append((
            perturbed_bitstring, perturbed_organism.fitness))

    return nk_organism_mutation_map

#length_of_desired_genome = 16
#k_intra = 4
#k_total = 6
#bit = bin(random.getrandbits(length_of_desired_genome))[2:]
#bit = bit.rjust(length_of_desired_genome, '0')
#nk_model_type = nk_model.NKModelFactory()
#use_model = nk_model_type.non_consecutive_dependencies_multigene(
#   8, 2, k_intra, k_total)
#nk_org = nk_organism.Organism(bitstring.Bitstring(bit), use_model)

#print nk_organism_mutation_map(nk_org, use_model)


def rna_organism_mutation_map(organism):
    """
    mutates every possible single step mutation from a intial
    organism of the correct type passed in. Returns a
    list of lists of tuples where each tuple is an rna_organism and its
    corresponding fitness.
    """
    rna_seq = organism.value
    rna_organism_mutation_map = []
    for i in range(len(rna_seq)):
        perturbed_org_list = organism.change_base(i)
        for org in perturbed_org_list:
            rna_organism_mutation_map.append((org, org.fitness))

    return rna_organism_mutation_map

rna_org = rna_organism.random_organism()
print rna_organism_mutation_map(rna_org)
