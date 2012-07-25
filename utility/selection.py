"""
Module to perform fitness proportional selection
Selection is based off number line proportionallity
If random number is selected in area that has already been selected
   the space in the population will be returned unfilled

Birth-death models:
Moran: Random death, among neighbors (well mixed for everyone) pick org
to give birth into that slot do it 1,000 times for a population size of 1,000.
This is termed a "generation"
"""
import random


def select(organisms, number_of_draws):
    new_population = []
    numberlined = numberline(organisms)
    already_added = object()
    for n in range(number_of_draws):
        for (i, (org, cum_fit)) in enumerate(numberlined):
            if random.random() < cum_fit:
                if org is not already_added:
                    new_population.append(org)
                    numberlined[i][0] = already_added
                break
    return new_population


def numberline(orgs):
    """
    Takes a list of organisms and returns
    a list of pairs in organism, cumulative
    normalized fitness
    """
    probs = []
    fitnesses = [org.fitness for org in orgs]
    norm_fits = normalize(fitnesses)
    probs.append(norm_fits[0])
    for i in range(1, len(fitnesses)):
        probs.append(probs[-1] + norm_fits[i])
    pairs = zip(orgs, probs)
    result = [[org, prob] for org, prob in pairs]
    result[-1][-1] = 1.0
    return result


def normalize(nums):
    """
    Normalizes a list of numbers so they sum to 1
    """
    total = float(sum(nums))
    return [(num / total) for num in nums]


def moran_death_birth(orgs, mutation_rate):
    """Method to execute the replacement of organism in a death-birth
    fashion using fecundity to replace the randomly seleted death organism
    """
    for _ in range(len(orgs)):
        index_to_kill = random.randrange(len(orgs))
        chosen_to_give_birth = fecundity_birth_selection(orgs)
        if random.random() < mutation_rate:
            chosen_to_give_birth = chosen_to_give_birth.mutate()
        orgs[index_to_kill] = chosen_to_give_birth
    return orgs


def fecundity_birth_selection(orgs):
    """Method to select an organism based off its fitness
    to replace death organism"""
    numberlined = numberline(orgs)
    for (i, (org, cum_fit)) in enumerate(numberlined):
        if random.random() < cum_fit:
            return org
