from os import popen, name


def w_latency_time(hostname):
    ping_report = [line.split() for line in popen("ping -n 1 " + hostname)]
    return int(ping_report[-1][-2])

def l_latency_time(hostname):
    ping_report = [line.split() for line in popen("ping -c 1 -q " + hostname)]
    return int(float(ping_report[-1][-2].split("/")[1]))

latency_time = w_latency_time if name == "nt" else l_latency_time
