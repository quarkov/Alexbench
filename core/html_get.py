import requests
import time as t


def html_get(hostname):
    start = t.time()
    requests.get("https://" + hostname)
    finish = t.time()
    return int((finish - start)*1000)
