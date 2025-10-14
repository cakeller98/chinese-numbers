from chinese_numbers.arabic import ArabicNumber
import pytest

def test_group_digits():
    # 1234567890 -> ['12', '3456', '7890'] (Chinese grouping: right to left, 4 digits per group)
    a = ArabicNumber('1234567890')
    assert a.groups == ['12', '3456', '7890'], f"Unexpected groups: {a.groups}"

    b = ArabicNumber('10000000000000000')
    assert b.groups == ['1', '0000', '0000', '0000', '0000'], f"Unexpected groups: {b.groups}"

    c = ArabicNumber('0')
    assert c.groups == ['0'], f"Unexpected groups: {c.groups}"

def test_idiomatic_overrides():
    a = ArabicNumber('10000000000000000')
    assert a.get_idiomatic_override() is not None
    b = ArabicNumber('100000000000000000')
    assert a.get_idiomatic_override() != b.get_idiomatic_override()
    c = ArabicNumber('123456')
    assert c.get_idiomatic_override() is None

@pytest.mark.parametrize("raw,expected", [
    ("000123", "123"),
    (" 1 2 3 ", "123"),
    ("1,234", "1234"),
    ("0", "0"),
])
def test_clean_number_string(raw, expected):
    a = ArabicNumber(raw)
    assert a.raw == expected

@pytest.mark.parametrize("bad_input", [
    "abc", "12a3", "1.23", "-123", "12 34a", ""
])
def test_invalid_input_raises(bad_input):
    with pytest.raises(ValueError):
        ArabicNumber(bad_input)
