import random
 
def select(population, fitness, num):
     total_fit = float(sum(fitness))
     rel_fitness = [f/total_fit for f in fitness]
            
     prob = [sum(rel_fitness[:i+1]) for i in range(len(rel_fitness))]
            
     new_population = []
     for n in xrange(num):
         r = random.random()
         for (i, individual) in enumerate(population):
             if r<= prob[i]:
                 new_population.append(individual)
                 prob.pop(i)
                 population.pop(i)
                 break
     return new_population 
