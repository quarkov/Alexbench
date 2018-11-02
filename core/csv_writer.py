import csv


class csvWriter:
    def __init__(self, filename, rows):
        self._results = open(filename + ".csv", "a")
        csv.writer(self._results).writerows([rows])

    def write(self, data):
        csv.writer(self._results).writerows([[d.value() for d in data] + [data[1].msg()]])

    def close(self):
        self._results.close()
