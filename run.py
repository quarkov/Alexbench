from core.functions import*
from core.classes import*
import os
import time

hostname = [input_hostname()]
duration, freq = input_params()
latency, perform = [], []
latency_time = w_latency_time if os.name == "nt" else l_latency_time

for i in range(duration*60//freq):
    start = time.time()
    lat_thread = ThreadValue(target=latency_time, args=hostname)
    per_thread = ThreadValue(target=page_loading, args=hostname)
    sleep_thread = ThreadValue(target=time.sleep, args=[freq])
    lat_thread.start(), per_thread.start(), sleep_thread.start()
    latency.append(lat_thread.join()), perform.append(per_thread.join()), sleep_thread.join()
    print("ok", time.time() - start)

print("ping:", latency)
print("loading:", perform)
