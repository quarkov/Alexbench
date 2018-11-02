from time import *
from core.metrics.base_metric import*


class TimeGet(BaseMetric):
    name = "clock"

    def __init__(self, hostname):
        BaseMetric.__init__(self, hostname)
        self._res = "00:00:00"

    def run(self):
        self._res = ctime(time()).split()[-2]
