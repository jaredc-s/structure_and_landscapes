from numpy import *
from pylab import *
from matplotlib import *
from scipy import *


def plot_average_fitness(fitness):
    values = [average_gen(gen) for gen in fitness]

    xlabel("Updates")
    ylabel("Average Fitness")
    plot(values)
    show()


def average_gen(generation_fitness):
    return average(generation_fitness)
