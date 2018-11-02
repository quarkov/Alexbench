from core.plots import PlotWriter


class Result:
    def __init__(self, name, msg, value, checked_value):
        self._name = name
        self._msg = msg
        self._value = value
        self._checked_value = checked_value

    def name(self):
        return self._name

    def msg(self):
        return self._msg

    def value(self):
        return self._value

    def checked_value(self):
        return self._checked_value


class ResultList:
    length = PlotWriter.bar_limit
    def __init__(self):
        self._res_list = [[Result('00:00:00', '', 0, 0)]]*self.length

    def add(self, data):
        self._res_list = self._res_list[1:]
        self._res_list.append(data)

    def data(self):
        return self._res_list
