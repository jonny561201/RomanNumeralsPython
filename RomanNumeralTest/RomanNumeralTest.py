import unittest
from RomanNumeral.RomanNumeral import RomanNumeral


class RomanNumeralTest(unittest.TestCase):

    def setUp(self):
        self.romanNumeral = RomanNumeral()

    def test_convertReturnsIWhenProvidedOne(self):
        actual = self.romanNumeral.Convert(1)
        self.assertEqual(actual, "I")
