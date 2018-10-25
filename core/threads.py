from threading import Event, Thread, Lock
from time import time, sleep


class ThreadValue(Thread):
    def __init__(self, fun, args, nmax):
        Thread.__init__(self)
        self._fun = fun
        self._args = args
        self._result = None
        self._event = Event()
        self._nmax = nmax

    def run(self):
        for i in range(self._nmax):
            self._event.wait()
            self._result = self._fun(self._args)
            self._event.clear()

    def result(self):
        return self._result

    def event(self):
        self._event.set()

    def is_event(self):
        return self._event.is_set()


class ThreadList:
    def __init__(self, nmax):
        self._list = []
        self._nmax = nmax

    def add(self, fun, arg):
        thr = ThreadValue(fun, arg, self._nmax)
        thr.start()
        self._list.append(thr)

    def run(self):
        [thr.event() for thr in self._list]

    def wait(self):
        while any([thr.is_event() for thr in self._list]):
            sleep(0.05)

    def result(self):
        res = []
        [res.append(thr.result()) for thr in self._list]
        return res

    def print_list(self):
        [print(thr) for thr in self._list]
