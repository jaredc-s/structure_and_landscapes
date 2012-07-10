from nk_organism import Organism
import bitstring_organism
import numpy
import random
import matplotlib.pyplot as plot
from bitstring import Bitstring
import nk_model

final_fit = []
orig_fit = []
non_con = []
nk = nk_model.NKModelFactory()
len_desired_genome = 20
non_con_multi = nk.non_consecutive_dependencies_multigene(5, 4, 3, 6)
con_multi = nk.consecutive_dependencies_multigene(5, 4, 3, 3)
for j in range(500):
    bit = bin(random.getrandbits(len_desired_genome))[2:]
    bit = bit.rjust(len_desired_genome, '0')

    org = Organism(Bitstring(bit), non_con_multi)
    org3 = Organism(Bitstring(bit), con_multi)
    orig_fit.append(org.fitness)
    for i in range(1000):
        org2 = org.mutate()
        org4 = org2.mutate()
        if org2.fitness > org.fitness:
            org = org2
        if org4.fitness > org3.fitness:
            org3 = org4
    final_fit.append(org.fitness)
    non_con.append(org3.fitness)
plot.figure(1)
plot.subplot(311)
plot.hist(orig_fit)
plot.subplot(312)
plot.hist(final_fit)
plot.subplot(313)
plot.hist(non_con)
plot.show()
