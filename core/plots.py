import numpy as np
from matplotlib import pyplot as plt


def plot_init(filename, tests_number):
    fig, ax = plt.subplots(figsize=(10, 0.5 * tests_number))
    ax.set_title(filename, size=14)
    ax.set_xlabel('time, ms')
    ax.set_xlim(0, 2000)
    ax.set_xticks(list(range(0, 2100, 100)), minor=True)
    ax.xaxis.grid(True)
    ax.invert_yaxis()
    ind = np.arange(tests_number)
    p = plt.barh(ind, 0, height=0.6, color='blue')
    l = plt.barh(ind, 0, height=0.6, color='green')
    plt.legend((p, l), ('loading time, ms', 'ping, ms'), loc=1)
    plt.savefig(filename + ".svg")
    return fig, ax

def plot_update(filename, fig, i, clock, loading, latency, status):

    if all([status == 200, loading <= 1950]):
        plt.barh(clock, loading, color='blue', height=0.6)
    if all([status == 200, loading > 1950]):
        title = "status.code - " + str(status) + ", loading time - " + str(loading) + " ms"
        plt.barh(i, 1950, color='red', height=0.6)
        plt.text(1300, i, title, fontsize='small', va='baseline')
    if status != 200:
        title = "can't get web page, status.code - " + str(status)
        plt.barh(i, loading, color='red', height=0.6)
        plt.text(510, i, title, fontsize='small', va='baseline')

    if latency:
        plt.barh(clock, latency, color='green', height=0.8)
    else:
        title = "response time is exceeded"
        plt.barh(clock, 15, color='black', height=0.8)
        plt.text(20, i, title, fontsize='small', va='baseline')

    fig.canvas.draw()
    plt.savefig(filename + ".svg")
