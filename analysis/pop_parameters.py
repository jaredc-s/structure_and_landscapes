from structure_and_landscapes.population import structure_population
from structure_and_landscapes.population import population
from structure_and_landscapes.bitstring import nk_organism
from structure_and_landscapes.bitstring import nk_model
import random
from structure_and_landscapes.bitstring.bitstring import Bitstring

len_desired_genome = 16
k_intra = 4
k_total = 6
bit = bin(random.getrandbits(len_desired_genome))[2:]
bit = bit.rjust(len_desired_genome, '0')
nk = nk_model.NKModelFactory()
use_model = nk.non_consecutive_dependencies_multigene(8, 2, k_intra, k_total)

org = nk_organism.Organism(Bitstring(bit), use_model)

pop = population.Population([org for _ in range(50)], 0.05)
struct = structure_population.Structured_Population([pop for _ in range(50)],
                                                    0.2, 0.1)

only_pop = population.Population([org for _ in range(500)], 0.05)
avg = []
struct_avg = []
for gen in range(250):
    sum = 0
    struct_sum = 0
    for org in only_pop:
        sum += org.fitness
    avg.append(sum / 2500.0)
    for pop in struct:
        for org in pop:
            struct_sum += org.fitness
    struct_avg.append(struct_sum / 2500.0)
    struct.advance_generation()
    only_pop.advance_generation()
    print "Gen: {}".format(gen)

#print avg
print
print
print struct_avg
