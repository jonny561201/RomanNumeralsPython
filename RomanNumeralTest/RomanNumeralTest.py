import unittest
from RomanNumeral.RomanNumeral import RomanNumeral


class RomanNumeralTest(unittest.TestCase):

    def setUp(self):
        self.romanNumeral = RomanNumeral()

    def test_convert__returns_i_when_provided_one(self):
        actual = self.romanNumeral.convert(1)
        self.assertEqual("I", actual)

    def test_convert__returns_ii_when_provided_two(self):
        actual = self.romanNumeral.convert(2)
        self.assertEqual("II", actual)

    def test_convert__returns_iii_when_provided_three(self):
        actual = self.romanNumeral.convert(3)
        self.assertEqual("III", actual)

    def test_convert__returns_iv_when_provided_four(self):
        actual = self.romanNumeral.convert(4)
        self.assertEqual("IV", actual)

    def test_convert__returns_v_when_provided_five(self):
        actual = self.romanNumeral.convert(5)
        self.assertEqual("V", actual)

    def test_convert__returns_vi_when_provided_six(self):
        actual = self.romanNumeral.convert(6)
        self.assertEqual("VI", actual)

    def test_convert__returns_ix_when_provided_nine(self):
        actual = self.romanNumeral.convert(9)
        self.assertEqual("IX", actual)

    def test_convert__returns_x_when_provided_ten(self):
        actual = self.romanNumeral.convert(10)
        self.assertEqual("X", actual)

    def test_convert__returns_xl_when_provided_forty(self):
        actual = self.romanNumeral.convert(40)
        self.assertEqual("XL", actual)

    def test_convert__returns_l_when_provided_fifty(self):
        actual = self.romanNumeral.convert(50)
        self.assertEqual("L", actual)

    def test_convert__returns_xc_when_provided_ninety(self):
        actual = self.romanNumeral.convert(90)
        self.assertEqual("XC", actual)

    def test_convert__returns_c_when_provided_one_hundred(self):
        actual = self.romanNumeral.convert(100)
        self.assertEqual("C", actual)