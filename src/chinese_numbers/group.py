# ChineseNumberGroup: represents a 4-digit group and its local Chinese representation
from .digits import get_digits, get_units, get_big_units

class ChineseNumberGroup:
    def __init__(self, group_str, index, total_groups, traditional=True):
        self.group_str = group_str.zfill(4)
        self.index = index
        self.total_groups = total_groups
        self.traditional = traditional
        self.value = int(group_str)
        self.is_zero = self.value == 0
        self.big_unit = get_big_units(traditional)[total_groups - index - 1] if not self.is_zero else ""
        self.local_repr = self._to_local()

    def _to_local(self):
        digits = get_digits(self.traditional)
        units = get_units(self.traditional)
        # Special case: exactly 10
        if self.index == 0 and self.group_str == '0010':
            return units[1]  # '十'
        # Special case: 11-19 (0011-0019)
        if self.index == 0 and self.group_str[:2] == '00' and self.group_str[2] == '1' and self.group_str[3] != '0':
            return units[1] + digits[int(self.group_str[3])]
        result = []
        zero_flag = False
        for i, char in enumerate(self.group_str):
            digit = int(char)
            unit_idx = 3 - i
            if digit == 0:
                if result:
                    zero_flag = True
                continue
            if zero_flag:
                result.append(digits[0])
                zero_flag = False
            # Default case
            result.append(digits[digit] + units[unit_idx])
        return ''.join(result)
