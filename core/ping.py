from os import popen, name


def w_latency_time(hostname):
    ping_report = [line.split() for line in popen("ping -n 1 -w 1000 " + hostname)]
    try:
        latency = int(ping_report[-1][-2])
    except (ValueError, IndexError):
        latency = 0
    return latency


def l_latency_time(hostname):
    ping_report = [line.split() for line in popen("ping -c 1 -q -W 1 " + hostname)]
    try:
        latency = int(float(ping_report[-1][-2].split("/")[1]))
    except (ValueError, IndexError):
        latency = 0
    return latency


latency_time = w_latency_time if name == "nt" else l_latency_time
