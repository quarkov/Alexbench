from os import popen, name
from core.metrics.base_metric import*

class LatencyGet(BaseMetric):
    name = "latency"

    def __init__(self, hostname):
        BaseMetric.__init__(self, hostname)
        self._res_min = 15

    def _cmd(self):
        return "ping -n 1 -w 1000 " if name == "nt" else "ping -c 1 -q -W 1 "

    def _parse(self, report):
        result = report[-1][-2]
        return result if name == "nt" else float(result.split("/")[1])

    def _check(self):
        return self._res if self._res else self._res_min

    def _msg(self):
        return "" if self._res else "response time is exceeded"

    def run(self):
        ping_report = [line.split() for line in popen(self._cmd() + self._addr)]
        try:
            self._res = int(self._parse(ping_report))
        except (ValueError, IndexError):
            self._res = 0
