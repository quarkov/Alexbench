import matplotlib.pyplot as plt
import numpy as np
from core.functions import*
from core.classes import*
import os
import csv

latency_time = w_latency_time if os.name == "nt" else l_latency_time

hostname = input_hostname()
duration, freq = input_params()

filename = store_dir(hostname)
results = open(filename, "a")
csv.writer(results).writerows([['time', 'ping', 'load']])
tests_number = duration*60//freq + 1


fig, ax = plt.subplots()

ax.set_title(filename.split('.')[0], size=20)
ax.set_xlabel('time, ms')
ax.xaxis.grid(True)
ax.invert_yaxis()
ind = np.arange(tests_number)
p = plt.barh(ind, 0, height=0.5, color='blue')
l = plt.barh(ind, 0, height=0.5, color='green')
plt.legend((l, p), ('ping', 'loading time'), loc=4)
plt.show(block = False)


for test in range(tests_number):
    start = time.time()
    lat_thread = ThreadValue(target=latency_time, args=[hostname])
    per_thread = ThreadValue(target=page_loading, args=[hostname])
    sleep_thread = ThreadValue(target=time.sleep, args=[freq])
    lat_thread.start(), per_thread.start(), sleep_thread.start()
    clock, latency, load = now(), lat_thread.join(), per_thread.join()
    print(clock)
    csv.writer(results).writerows([[clock, latency, load]])
    p = plt.barh(clock, load, color='blue', height=0.5)
    l = plt.barh(clock, latency, color='green', height=0.5)
    print(clock)

    fig.canvas.draw_idle()
    try:
        fig.canvas.flush_events()
    except NotImplementedError:
        pass

    sleep_thread.join()
    print("ok", time.time() - start)
results.close()
