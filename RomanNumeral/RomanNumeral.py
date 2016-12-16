class RomanNumeral(object):
    unique_roman_characters = {
        1: "I",
        4: "IV",
        5: "V",
        9: "IX",
        10: "X",
        40: "XL",
        50: "L",
        90: "XC",
        100: "C",
        900: "CM",
        1000: "M",
    }

    def convert(self, arabic_numeral):
        response = ""
        for value, char in sorted(self.unique_roman_characters.iteritems(), reverse=True):
            if value <= arabic_numeral:
                while arabic_numeral >= value:
                    arabic_numeral -= value
                    response += char

        return response
