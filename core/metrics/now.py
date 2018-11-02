from time import *
from core.base_metric import*


class TimeGet(BaseMetric):
    name = "clock"

    def __init__(self, hostname):
        BaseMetric.__init__(self, hostname)
        self._res = "00:00:00"

    def _msg(self):
        return ""

    def _check(self):
        return self._res

    def run(self):
        self._res = ctime(time()).split()[-2]


    # def now():
    #     return ctime(time()).split()[-2]
