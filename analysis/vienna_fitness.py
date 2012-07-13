from structure_and_landscapes.rna import rna_organism
from structure_and_landscapes.rna import vienna_distance
import matplotlib.pylab 
import random


def hill_climb(rna_org):
   count = 0
   fitnesses = []
   goal =  vienna_distance.fold(rna_organism.OPTIMAL_RNA_SEQUENCE)
   while True:
      pos_map = []
      print
      print rna_org.value
      print vienna_distance.fold(rna_org.value)
      for _ in range(len(rna_org.value)*4):
         rna_org2 = rna_org.mutate()
         pos_map.append(tuple([rna_org2.fitness, rna_org2]))
      
      print rna_org.fitness, max(pos_map)[0]
      if rna_org.fitness == 1:
         print rna_org.value
         print rna_organism.OPTIMAL_RNA_SEQUENCE
         print count
         matplotlib.pyplot.plot(fitnesses)
         matplotlib.pyplot.show()
         break

      elif max(pos_map) > rna_org.fitness:
         rna_org = max(pos_map)[1]
         count += 1
         fitnesses.append(rna_org.fitness)
      else:
         print rna_org.value
         print rna_organism.OPTIMAL_RNA_SEQUENCE
         break




seq = [random.choice(['A']) for _ in range(rna_organism.RNA_SEQUENCE_LENGTH)]
seq = "".join(seq)
print len(seq)
org = rna_organism.random_organism()
hill_climb(org)
