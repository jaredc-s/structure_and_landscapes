from numpy import *
from pylab import *
from matplotlib import *
import matplotlib.pyplot as plt
from scipy import *


def plot_average_fitness(fitness):
    values = [average(gen) for gen in fitness]

    xlabel("Updates")
    ylabel("Average Fitness")
    plot(values)
    show()

def plot_fitness_distribution(fitness_list):
    mu, sigma = 100, 15
    x = mu + sigma * numpy.random.randn(100000)

    fig = plt.figure()
    ax = fig.add_subplot(111)
    n, bins, patches = ax.hist(x, 50, normed=1, facecolor='green', alpha=.75)

