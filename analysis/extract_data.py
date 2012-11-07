from structure_and_landscapes import persistence
from structure_and_landscapes.persistence import run
from structure_and_landscapes.persistence import persistence
from scipy import stats

"""
write tests...
"""

shelf_path = '/vagrant/saved_runs.dat'
run_list = list(persistence.values(shelf_path))

def filter_run_list(run_list, parameters_dictionary):
    """
    takes a list of runs and filters them by specified parameters
    passed in. Retruns a list of filtered runs.
    """
    filtered_run_list = run_list

    for run in run_list:
        for key in parameters_dictionary.keys():
            if run.parameters[key] != parameters_dictionary[key]:
                filtered_run_list.remove(run)
                break

    return filtered_run_list

def organism_fitness_for_each_run(run_list):
    """
    returns a list of lists where the nested list holds all organisms final fitness. The
    outer list carries each run.
    """
    org_fitness_list = []
    sub_population_fitness_list = []
    for run in run_list:
        for sub_population in run.final_population:
            for org in sub_population:
                org_fitness_list.append(org.fitness)
            sub_population_fitness_list.append(org_fitness)
            org_fitness = []

    return sub_population_fitness_list

def variance_fitness_for_each_run(population_fitness_list):
    """
    to be finished
    """
    variance_fitness_list = []
    for sub_population_fitness_list in population_fitness_list:
        variance_fitness_list.append(stats.

def mean_fitness_for_each_run(run_list):
    """
    returns a list of mean final fitnesses for each run
    """
    return [run.final_population.mean_fitness() for run in run_list]

def max_fitness_for_each_run(run_list):
    """
    returns a list of the max final fitness for each run
    """
    return [run.final_population.max_fitness() for run in run_list]

#Call
mean_list = mean_fitness_for_each_run(run_list)
print mean_list

#filtered_run_list = filter_run_list(run_list, {'Organism Type':'NK Model'})
#print organism_fitness_for_each_run(filtered_run_list)
