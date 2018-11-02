import requests
import time as t
from core.metrics.base_metric import*


class HtmlGet(BaseMetric):
    name = "htmlGet"

    def __init__(self, hostname):
        BaseMetric.__init__(self, hostname)
        self._code = 0
        self._res_max = 1950

    def _check(self):
        return self._res if self._res <= self._res_max else self._res_max

    def _msg(self):
        if self._code != 200:
            return "can't get web page; code - " + str(self._code)
        elif self._res > self._res_max:
            return "code - " + str(self._code) + "; loading time - " + str(self._res) + " ms"
        else:
            return ""

    def run(self):
        try:
            start = t.time()
            page = requests.get("http://" + self._addr)
            finish = t.time()
            self._code = page.status_code
            self._res = int((finish - start)*1000) if self._code == 200 else 0
        except requests.exceptions:
            self._code = 0
            self._res = 0
