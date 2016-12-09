import unittest
from RomanNumeral.RomanNumeral import RomanNumeral


class RomanNumeralTest(unittest.TestCase):

    def setUp(self):
        self.romanNumeral = RomanNumeral()

    def test_convertReturnsIWhenProvidedOne(self):
        actual = self.romanNumeral.Convert(1)
        self.assertEqual(actual, "I")

    def test_ConvertReturnsIIWhenProvidedTwo(self):
        actual = self.romanNumeral.Convert(2)
        self.assertEqual(actual, "II")

    def test_ConvertReturnsIIIWhenProvidedThree(self):
        actual = self.romanNumeral.Convert(3)
        self.assertEqual(actual, "III")

    def test_ConvertReturnsIVWhenProvidedFour(self):
        actual = self.romanNumeral.Convert(4)
        self.assertEqual(actual, "IV")

    def test_ConvertReturnsVWhenProvidedFive(self):
        actual = self.romanNumeral.Convert(5)
        self.assertEqual(actual, "V")

    def test_ConvertReturnsVIWhenProvidedSix(self):
        actual = self.romanNumeral.Convert(6)
        self.assertEqual(actual, "VI")
