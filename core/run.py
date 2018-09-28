from core.functions import w_latency_time, l_latency_time, page_loading
import os
import time

print("input hostname (e.i. 'google.com')")
hostname = input()
print("ok, input measurement duration and frequency in seconds")
duration, freq = map(int, (input().split()))
latency, perform = [], []

for i in range(duration*60//freq):
    latency.append(w_latency_time(hostname) if os.name == "nt" else l_latency_time(hostname))
    perform.append(page_loading(hostname))
    time.sleep(freq)
    print("ok")

print(latency)
print(perform)
