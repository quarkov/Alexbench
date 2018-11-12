from unittest.mock import patch
from io import StringIO
from unittest import TestCase
from core.inputs import*


class TestInputHostname(TestCase):

    msg_wrong = "incorrect hostname, try again\n"*3 + "hostname is set by default: gdansk.pl"

    @staticmethod
    def run_input_hostname(mock_input, expected_out):
        with patch("builtins.input", return_value=mock_input), patch("sys.stdout", new=StringIO()) as fake_output:
            input_hostname()
            return fake_output.getvalue().strip(), expected_out

    def test_skip_hostname(self):
        income, outcome = self.run_input_hostname("", "hostname is set as gdansk.pl")
        self.assertEqual(income, outcome)

    def test_positive_hostname(self):
        self.pos_list = [
                        "dynatrace.com",
                        "gdansk.pl",
                        "spacex.com",
                        "zortrax.com"
                        ]
        for hs in self.pos_list:
            income, outcome = self.run_input_hostname(hs, "hostname is set as " + hs)
            self.assertEqual(income, outcome)

    def test_negative_hostname(self):
        self.neg_list = [
                        ".",
                        "..",
                        "...",
                        ".com",
                        "a.",
                        ",",
                        "-",
                        ".11",
                        "0",
                        "gaevnjsm, "
                        "645erdfvc%"
                        ]
        for hs in self.neg_list:
            income, outcome = self.run_input_hostname(hs, self.msg_wrong)
            self.assertEqual(income, outcome)


class TestInputDigits(TestCase):

    msg_out_of_scope = "1440 >= an integer >= 1 is expected, try again\n" * 3 + "value is set by default: 1"
    msg_wrong_input = "it's not an integer, try again\n" * 3 + "value is set by default: 1"

    @staticmethod
    def run_input_digits(mock_input, expected_out):
        with patch("builtins.input", return_value=mock_input), patch("sys.stdout", new=StringIO()) as fake_output:
            digit_input(1, 1440, 1)
            return fake_output.getvalue().strip(), expected_out

    def test_skip_digits(self):
        income, outcome = self.run_input_digits("", "")
        self.assertEqual(income, outcome)

    def test_positive_digits_out_of_scope(self):
        self.pos_digs = [
                        "0",
                        "0000"
                        "1441",
                        "-10",
                        "2000"
                        ]
        for number in self.pos_digs:
            income, outcome = self.run_input_digits(number, self.msg_out_of_scope)
            self.assertEqual(income, outcome)

    def test_negative_digits_input(self):
        self.pos_digs = [
                        " ",
                        ".",
                        "as10",
                        "0o1%",
                        "1.5",
                        "1,5"
                        ]
        for number in self.pos_digs:
            income, outcome = self.run_input_digits(number, self.msg_wrong_input)
            self.assertEqual(income, outcome)
