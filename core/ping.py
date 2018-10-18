from os import popen


def w_latency_time(hostname):
    ping_report = [line.split() for line in popen("ping -n 10 " + hostname)]
    return int(ping_report[-1][-2])


def l_latency_time(hostname):
    ping_report = [line.split() for line in popen("ping -c 10 -q " + hostname)]
    return int(float(ping_report[-1][-2].split("/")[1]))
