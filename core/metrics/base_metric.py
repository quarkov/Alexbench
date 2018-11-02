from core.metrics.results import Result


class BaseMetric:
    name = ""

    def __init__(self, hostname):
        self._addr = hostname
        self._res = None

    def _msg(self):
        return ""

    def _check(self):
        return self._res

    def result(self):
        return Result(self.name, self._msg(), self._res, self._check())
