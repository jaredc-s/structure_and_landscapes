from structure_and_landscapes.run_management import run
from structure_and_landscapes.run_management import persistence
from scipy import stats
import itertools

"""
write tests...
go through all runs just once and pull out data!
"""


def filter_runs(runs, parameters_dictionary):
    """
    """
    def same_parameters(run):
        same_values = [run.parameters.get(key) == value
                       for key, value in parameters_dictionary.items()]
        return all(same_values)
    return itertools.ifilter(same_parameters, runs)


def organism_fitness_for_each_run(runs):
    """
    """
    def sub_population_fitness(sub_population):
        for org in sub_population:
            yield org.fitness

    for run in runs:
        for sub_population in run.final_population:
            yield sub_population_fitness(sub_population)


def mean_fitness_for_each_run(runs):
    """
    """
    return [run.final_population.mean_fitness() for run in runs]


def max_fitness_for_each_run(run_list):
    """
    """
    return [run.final_population.max_fitness() for run in run_list]


if __name__ == "__main__":
    shelf_path = '/vagrant/saved_runs.dat'
    runs = persistence.values(shelf_path)

    filtered_runs = filter_runs(runs, {'Organism Type': 'NK Model'})
    #runs1, runs2 = itertools.tee(filtered_runs, 2)
    #print mean_fitness_for_each_run(runs1)
    #print max_fitness_for_each_run(runs2)
    #population_fitness = list(organism_fitness_for_each_run(filtered_runs))
    #print map(list, population_fitness)
