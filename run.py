from core.html_get import*
from core.inputs import*
from core.now import*
from core.ping import latency_time
from core.plots import*
from core.store_dir import*
from core.threads import*
from core.web_page_open import*
from time import time, sleep
import csv


hostname = input_hostname()
duration, freq = input_params()

filename = store_dir(hostname)
tests_number = duration*60//freq + 1

results = open(filename + ".csv", "a")
csv.writer(results).writerows([['time', 'ping', 'load']])

fig, ax = plot_init(filename, tests_number)
web_page_open(filename, freq, tests_number)

thrs = ThreadList(tests_number)
[thrs.add(func, hostname) for func in [latency_time, html_get]]

for i in range(tests_number):
    start = time()
    thrs.run()
    thrs.wait()
    latency, [loading, status] = thrs.result()
    print("thread end=", time()-start)
    csv.writer(results).writerows([[now()] + thrs.result()])
    print("csv write=", time()-start)
    plot_update(filename, fig, i, now(), loading, latency, status)
    print("plot update=", time()-start)
    print("test", i+1, "has passed, tests remain:", tests_number-i-1)
    delta = time() - start
    print()
    sleep((freq - delta) if freq > delta else 0)

results.close()
