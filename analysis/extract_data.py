from structure_and_landscapes import persistence
from structure_and_landscapes.persistence import run
from structure_and_landscapes import persistence.run
from structure_and_landscapes.persistence import persistence

"""
what is highest fitnesss
mean fitness of shelf
mean fitness of more specific runs
"""

shelf_path = '/vagrant/saved_runs.dat'
shelf = persistence.get_shelf(shelf_path)

with shelf as shelf2:
    print shelf2

def highest_fitness_for_all_runs(run_list):
    """
    returns a list of mean final fitnesses for each run
    """
    return [run.final_population.mean_fitness() for run in run_list]


#runs = get_run_list(shelf_path)
#mean_list = highest_fitness_for_all_runs(runs)
#print runs
#print mean_list
