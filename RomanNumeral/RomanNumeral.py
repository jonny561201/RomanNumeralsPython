class RomanNumeral(object):
    unique_roman_characters = {
        5: "V",
        4: "IV",
        1: "I",
    }

    def convert(self, arabic_numeral):
        response = ""
        for value, char in self.unique_roman_characters.iteritems():
            if value <= arabic_numeral:
                while arabic_numeral >= value:
                    arabic_numeral -= value
                    response += char

        return response
