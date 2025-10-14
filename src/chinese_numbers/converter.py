# ChineseNumberConverter: orchestrates the conversion process
from .arabic import ArabicNumber
from .group import ChineseNumberGroup
from .digits import get_digits

class ChineseNumberConverter:
    def __init__(self, use_traditional=True):
        self.use_traditional = use_traditional

    def convert(self, num: str) -> str:
        arabic = ArabicNumber(num, self.use_traditional)
        if arabic.raw == "0":
            return get_digits(self.use_traditional)[0]
        idiomatic = arabic.get_idiomatic_override()
        if idiomatic:
            return idiomatic
        groups = [ChineseNumberGroup(g, i, len(arabic.groups), self.use_traditional) for i, g in enumerate(arabic.groups)]
        result = []
        for i, group in enumerate(groups):
            if group.is_zero:
                if i < len(groups) - 1 and not groups[i + 1].is_zero:
                    result.append(get_digits(self.use_traditional)[0])
                continue
            # Insert '零' if previous group is nonzero, current group has leading zeros, and is not all zero
            if i > 0 and not groups[i-1].is_zero and group.group_str[:3] == '000':
                result.append(get_digits(self.use_traditional)[0])
            elif i > 0 and not groups[i-1].is_zero and group.group_str[:2] == '00':
                result.append(get_digits(self.use_traditional)[0])
            elif i > 0 and not groups[i-1].is_zero and group.group_str[0] == '0':
                result.append(get_digits(self.use_traditional)[0])
            result.append(group.local_repr)
            if group.big_unit:
                result.append(group.big_unit)
        return ''.join(result)
