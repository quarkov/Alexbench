from unittest import TestCase
from core.metrics.ping import*
from time import sleep

class TestLatencyGet(TestCase):
    hs_list_pos = [
                  "google.com",
                  "gdansk.pl",
                  "spacex.com",
                  "blueorigin.com"
                  ]

    hs_list_neg = [
                  "dynatrace.com",
                  "zortrax.com"
                  ]


    def test_run_pos(self):
        for hs in self.hs_list_pos:
            test_obj = LatencyGet(hs)
            test_obj.run()
            self.assertTrue(test_obj.result().value() != 0)
            self.assertTrue(test_obj.result().msg() == "")
            sleep(1)

    def test_run_neg(self):
        for hs in self.hs_list_neg:
            test_obj = LatencyGet(hs)
            test_obj.run()
            self.assertTrue(test_obj.result().value() == 0)
            self.assertTrue(test_obj.result().msg() == "response time is exceeded")
            sleep(1)
