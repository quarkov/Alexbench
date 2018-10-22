from core.classes import*
from core.html_get import*
from core.inputs import*
from core.now import*
from core.ping import latency_time
from core.plots import*
from core.store_dir import*
from core.web_page_open import*
import csv


hostname = input_hostname()
duration, freq = input_params()

filename = store_dir(hostname)
tests_number = duration*60//freq + 1

results = open(filename + ".csv", "a")
csv.writer(results).writerows([['time', 'ping', 'load']])

fig, ax = plot_init(filename, tests_number)
web_page_open(filename, freq)

for test in range(tests_number):
    lat_thread = ThreadValue(target=latency_time, args=[hostname])
    per_thread = ThreadValue(target=html_get, args=[hostname])
    sleep_thread = ThreadValue(target=t.sleep, args=[freq])
    lat_thread.start(), per_thread.start(), sleep_thread.start()
    clock, latency, [loading, status] = now(), lat_thread.join(), per_thread.join()

    csv.writer(results).writerows([[clock, latency, loading]])
    plot_update(filename, fig, test, clock, loading, latency, status)
    sleep_thread.join()
    print("test", test+1, "has passed, tests remain:", tests_number-test-1)

results.close()