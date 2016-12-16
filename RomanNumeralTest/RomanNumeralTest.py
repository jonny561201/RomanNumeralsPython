import unittest
from RomanNumeral.RomanNumeral import RomanNumeral


class RomanNumeralTest(unittest.TestCase):

    def setUp(self):
        self.romanNumeral = RomanNumeral()

    def test_convertReturnsIWhenProvidedOne(self):
        actual = self.romanNumeral.convert(1)
        self.assertEqual("I", actual)

    def test_ConvertReturnsIIWhenProvidedTwo(self):
        actual = self.romanNumeral.convert(2)
        self.assertEqual("II", actual)

    def test_ConvertReturnsIIIWhenProvidedThree(self):
        actual = self.romanNumeral.convert(3)
        self.assertEqual("III", actual)

    def test_ConvertReturnsIVWhenProvidedFour(self):
        actual = self.romanNumeral.convert(4)
        self.assertEqual("IV", actual)

    def test_ConvertReturnsVWhenProvidedFive(self):
        actual = self.romanNumeral.convert(5)
        self.assertEqual("V", actual)

    def test_ConvertReturnsVIWhenProvidedSix(self):
        actual = self.romanNumeral.convert(6)
        self.assertEqual("VI", actual)

    def test_convert__returns_x_when_provided_ten(self):
        actual = self.romanNumeral.convert(10)
        self.assertEqual("X", actual)
