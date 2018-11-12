from unittest import TestCase
from core.metrics.html_get import*

class TestHtmlGet(TestCase):
    test_page = "httpbin.org/status/"
    codes = [
             "200",
             "400",
             "404",
             "414",
             "500",
             "502"
            ]

    def test_run(self):
        for code in self.codes:
            test_obj = HtmlGet(self.test_page+code)
            test_obj.run()
            if code != "200":
                self.assertFalse(test_obj.result().value())
                self.assertTrue(test_obj.result().msg() == "can't get web page; code - " + code)
            else:
                self.assertTrue(test_obj.result().value())

            print(test_obj.result().value(), test_obj.result().msg())
