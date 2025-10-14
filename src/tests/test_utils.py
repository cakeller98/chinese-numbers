import pytest
from chinese_numbers.utils import clean_number_string

@pytest.mark.parametrize("raw,locale_str,expected", [
    ("1,234,567", "en_US", "1234567"),
    ("1.234.567", "de_DE", "1234567"),
    ("1234567", "en_US", "1234567"),
    ("0001234567", "en_US", "1234567"),
    ("0", "en_US", "0"),
])
def test_clean_number_string_valid(raw, locale_str, expected):
    import locale
    try:
        if locale_str:
            locale.setlocale(locale.LC_ALL, locale_str)
    except locale.Error:
        print(f"WARNING: Locale '{locale_str}' unavailable, test not run for input '{raw}'")
        import pytest
        pytest.skip(f"Locale '{locale_str}' unavailable")
    assert clean_number_string(raw, locale_str) == expected

@pytest.mark.parametrize("raw,locale_str", [
    ("1,234.56", "en_US"),  # decimal in en_US
    ("1.234,56", "de_DE"),  # decimal in de_DE
    # ("1,23,456", "en_US"),  # invalid grouping
    # ("1.23.456", "de_DE"),  # invalid grouping
    ("abc123", "en_US"),    # non-numeric
    ("12a34", "en_US"),     # non-numeric
    ("1,234,567.0", "en_US"), # decimal zero
    ("1.234.567,0", "de_DE"), # decimal zero
    # ("1 234 567", "fr_FR"),    # spaces as group separator (not supported by locale.atoi)
])
def test_clean_number_string_invalid(raw, locale_str):
    with pytest.raises(ValueError):
        clean_number_string(raw, locale_str)
