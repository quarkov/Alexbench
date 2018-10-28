import requests
import time as t


def html_get(hostname):
    start = t.time()
    try:
        page = requests.get("http://" + hostname)
        finish = t.time()
        code = page.status_code
        return [int((finish - start)*1000), code] if code == 200 else [0, code]
    except requests.exceptions:
        return [0, 0]
