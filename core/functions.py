import os
import requests
import time


def w_latency_time(hostname):
    ping_report = [line.split() for line in os.popen("ping -n 10 " + hostname)]
    ping_delay = int(ping_report[-1][-2])
    return ping_delay


def l_latency_time(hostname):
    ping_report = [line.split() for line in os.popen("ping -c 10 -q " + hostname)]
    ping_delay = int(float(ping_report[-1][-2].split("/")[1]))
    return ping_delay


def page_loading(hostname):
    start = time.time()
    requests.get("https://" + hostname)
    finish = time.time()
    return int((finish - start)*1000)
