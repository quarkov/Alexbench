import numpy as np
from matplotlib import pyplot as plt


def plot_init(filename, tests_number):
    fig, ax = plt.subplots(figsize=(10, 0.3 * tests_number))
    ax.set_title(filename, size=14)
    ax.set_xlabel('time, ms')
    ax.set_xlim(0, 1600)
    ax.set_xticks(list(range(0, 1700, 100)), minor=True)
    ax.xaxis.grid(True)
    ax.invert_yaxis()
    ind = np.arange(tests_number)
    p = plt.barh(ind, 0, height=0.5, color='blue')
    l = plt.barh(ind, 0, height=0.5, color='green')
    plt.legend((p, l), ('ping, ms', 'loading time, ms'), loc=1)
    plt.savefig(filename + ".svg")
    return fig, ax

def plot_update(filename, fig, clock, loading, latency):
    plt.barh(clock, loading, color='blue', height=0.5)
    plt.barh(clock, latency, color='green', height=0.5)
    fig.canvas.draw()
    plt.savefig(filename + ".svg")
