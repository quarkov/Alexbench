from datetime import*
import os
import requests
import time


def input_hostname():
    hs = input("enter a hostname or press 'enter' to use default google.com: ")
    hostname = hs if hs else "google.com"
    print("hostname is set as", hostname)
    print()
    return hostname


def input_params():
    dr = input("enter test duration in minutes (int) or press 'enter' to use default 2: ")
    fr = input("enter frequency in seconds (int) or press 'enter' to use default 20: ")
    duration, freq = (int(dr), int(fr)) if all((dr, fr)) else (2, 20)
    print("test duration is set as", duration, "minutes,", "frequency is set as", freq, "seconds")
    print()
    return duration, freq


def store_dir(hostname):
    if "results" not in os.listdir():
        os.mkdir("results")
    os.chdir("results")

    if hostname not in os.listdir():
        os.mkdir(hostname)
    os.chdir(hostname)

    if str(len(os.listdir())+1) not in os.listdir():
        os.mkdir(str(len(os.listdir())+1))
    os.chdir(str(len(os.listdir())))

    filename = hostname.split(".")[0] + "_" + str(datetime.now()).split()[0] + "_" + str(len(os.listdir()))
    return filename


def now():
    return time.ctime(time.time()).split()[-2]


def w_latency_time(hostname):
    ping_report = [line.split() for line in os.popen("ping -n 10 " + hostname)]
    return int(ping_report[-1][-2])


def l_latency_time(hostname):
    ping_report = [line.split() for line in os.popen("ping -c 10 -q " + hostname)]
    return int(float(ping_report[-1][-2].split("/")[1]))


def page_loading(hostname):
    start = time.time()
    requests.get("https://" + hostname)
    finish = time.time()
    return int((finish - start)*1000)
