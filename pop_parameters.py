import structure_population
import population
import nk_organism
import nk_model
import random
from bitstring import Bitstring

len_desired_genome = 16
k_intra = 4
k_total = 0
bit = bin(random.getrandbits(len_desired_genome))[2:]
bit = bit.rjust(len_desired_genome, '0')
nk = nk_model.NKModelFactory()
use_model = nk.non_consecutive_dependencies_multigene(8, 2, k_intra, k_intra)

org = nk_organism.Organism(Bitstring(bit), use_model)

pop = population.Population([org for _ in range(50)])
struct = structure_population.Structured_Population([pop for _ in range(10)], 0.5, 0.5)

only_pop = population.Population([org for _ in range(500)])
avg = []
for gen in range(250):
    sum = 0
    for org in only_pop:
        sum += org.fitness
    avg.append(sum/50.0)
    #struct.advance_generation()
    only_pop.advance_generation()
    print "Gen: {}".format(gen)

print avg
