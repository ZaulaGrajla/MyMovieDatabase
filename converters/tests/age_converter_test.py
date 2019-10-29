import unittest
from converters.age_converter import StringIntoAgeConverter


class StringIntoAgeConverterTest(unittest.TestCase):

    def test_should_raise_error_when_wrong_dash(self):
        with self.assertRaises(IndexError):
            StringIntoAgeConverter("1231231233")
            StringIntoAgeConverter("1999:12-12")

    def test_should_raise_error_when_wrong_length_of_string(self):
        with self.assertRaises(ValueError):
            StringIntoAgeConverter("123")

    def test_should_raise_error_when_non_int_chars(self):
        with self.assertRaises(ValueError):
            StringIntoAgeConverter("1231-:2-:1")
            StringIntoAgeConverter("1234-dd-tt")

    def test_should_raise_error_when_spaces(self):
        with self.assertRaises(ValueError):
            StringIntoAgeConverter("1992- 9- 1")

    def test_should_raise_error_when_wrong_year(self):
        with self.assertRaises(ValueError):
            StringIntoAgeConverter("3000-12-12")

    def test_should_raise_error_when_wrong_month(self):
        with self.assertRaises(ValueError):
            StringIntoAgeConverter("2000-13-12")

    def test_should_raise_error_when_wrong_day(self):
        with self.assertRaises(ValueError):
            StringIntoAgeConverter("2000-12-32")

    def test_should_raise_error_when_not_leap_year(self):
        with self.assertRaises(ValueError):
            StringIntoAgeConverter("2017-02-29")

    def test_should_return_age(self):
        pass
