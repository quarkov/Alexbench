import requests
import time as t


def html_get(hostname):
    start = t.time()
    page = requests.get("https://" + hostname)
    finish = t.time()
    code = page.status_code
    return [int((finish - start)*1000), code] if code == 200 else [0, code]
