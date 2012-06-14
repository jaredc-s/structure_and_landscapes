"""
Module to perform fitness proportional selection
Selection is based off number line proportionallity
If random number is selected in area that has already been selected
   the space in the population will be returned unfilled
"""

import random


random_generator = random.Random()
 
def select(organisms, number_of_draws):
     
     new_population = []

     numberlined = numberline(organisms)

     already_added = object()

     for n in range(number_of_draws):
         for (i, (org, cum_fit)) in enumerate(numberlined):
             if random_generator.random() < cum_fit:
                  if org is not already_added:
                       new_population.append(org)
                       numberlined[i][0] = already_added
                  break
                 
     return new_population 

def numberline(orgs):
     """
     Takes a list of organisms and returns a list of pairs in organism, cumulative
     normalized fitness
     """
     fitnesses = [org.fitness for org in orgs]
     
     norm_fits = normalize(fitnesses)

     probs = [sum(norm_fits[:i+1]) for i in range(len(fitnesses))]
     pairs = zip(orgs, probs)

     result = [[org,prob] for org,prob in pairs]
     result[-1][-1] = 1.0
     
     return result
def normalize(nums):
     """
     Normalizes a list of numbers so they sum to 1
     """
     total = float(sum(nums))
     
     return [(num / total) for num in nums]
     
