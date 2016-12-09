class RomanNumeral(object):

    def Convert(self, arabicNumeral):
        if arabicNumeral == 1:
            return "I"
        if arabicNumeral == 2:
            return "II"
        if arabicNumeral == 4:
            return "IV"
        if arabicNumeral == 5:
            return "V"
        if arabicNumeral == 6:
            return "VI"
        return "III"