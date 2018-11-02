from core.metrics.html_get import*
from core.metrics.now import*
from core.metrics.ping import*
from core.metrics.results import*
from core.inputs import*
from core.plots import*
from core.store_dir import*
from core.threads import*
from core.web_page_open import*
from time import time, sleep
from core.csv_writer import*


class Scheduler:
    def __init__(self):
        hostname = input_hostname()
        duration, self._freq = input_params()
        self._testsCount = duration * 60 // self._freq + 1
        filename = store_dir(hostname)

        self._thrs = ThreadList(self._testsCount)
        metrics = [TimeGet, HtmlGet, LatencyGet]
        [self._thrs.add(metric(hostname)) for metric in metrics]

        self._csv = csvWriter(filename, [metric.name for metric in metrics] + ["status code"])
        self._plot = PlotWriter(filename)
        web_page_open(filename, self._freq, self._testsCount)

    def run(self):
        monitor_data = ResultList()
        for probe in range(self._testsCount):
            start = time()
            self._thrs.run()
            self._thrs.wait()
            record = self._thrs.result()
            self._csv.write(record)
            monitor_data.add(record)
            self._plot.update(monitor_data.data(), probe, self._testsCount)
            delta = time() - start
            sleep((self._freq - delta) if self._freq > delta else 0)

        self._csv.close()
