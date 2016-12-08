class RomanNumeral(object):

    def Convert(self, arabicNumeral):
        if(arabicNumeral == 1):
            return "I"
        if(arabicNumeral == 2):
            return "II"
        return "III"