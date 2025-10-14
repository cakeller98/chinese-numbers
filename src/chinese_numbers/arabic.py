# ArabicNumber: parses and groups Arabic numerals, detects idiomatic overrides
from .utils import clean_number_string
from .digits import get_digits, get_units, get_big_units

class ArabicNumber:
    def __init__(self, raw: str, traditional=True):
        self.raw = clean_number_string(raw)
        self.traditional = traditional
        self.groups = self._group_digits()
        self.length = len(self.raw)

    def _group_digits(self):
        num = self.raw
        segments = []
        while num:
            segments.append(num[-4:])
            num = num[:-4]
        segments.reverse()
        return segments

    def idiomatic_overrides(self):
        digits = get_digits(self.traditional)
        units = get_units(self.traditional)
        big = get_big_units(self.traditional)
        return {
            "10000000000000000": digits[1] + units[3] + big[1] + big[2],  # 一千萬億
            "100000000000000000": digits[1] + big[4],  # 一京
        }

    def get_idiomatic_override(self):
        return self.idiomatic_overrides().get(self.raw)

    def __str__(self):
        return self.raw
    
    def __repr__(self):
        return f"ArabicNumber(raw='{self.raw}', traditional={self.traditional})"