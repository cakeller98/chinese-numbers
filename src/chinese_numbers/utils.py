# Utility functions for the Chinese Numbers package
#  import re

# def old_clean_number_string(raw: str) -> str:
#     """Sanitize and validate the input string, removing commas and whitespace."""
#     s = str(raw).replace(',', '').replace(' ', '')
#     if not re.fullmatch(r'\d+', s):
#         raise ValueError(f"Invalid input: {raw}")
#     return s.lstrip('0') or '0'

import locale

def clean_number_string(raw: str, locale_str: str = '', ultra_strict: bool = False) -> str:
    """
    Parse a locale-formatted integer string (e.g. '1.234.567' in German, '1,234,567' in US) to a plain digit string.
    Decimals (comma in de_DE, period in en_US) are not allowed and will raise an error.
    Optionally specify a locale string (e.g. 'de_DE', 'en_US'). Defaults to user's locale if not provided.
    By default, spaces are stripped before parsing. Set ultra_strict=True to disable this and require exact locale formatting.
    """
    s = str(raw)
    if not ultra_strict:
        s = s.replace(' ', '')
        print(f"DEBUG: clean_number_string: stripped spaces: '{s}'")
    if locale_str:
        locale.setlocale(locale.LC_ALL, locale_str)
    else:
        locale.setlocale(locale.LC_ALL, '')  # Use user's locale settings
    try:
        number = locale.atoi(s)
        if not isinstance(number, int) or number < 0:
            print(f"DEBUG: clean_number_string: invalid number: '{s}'")
            raise ValueError(f"Invalid input: {raw}")
        return str(number)
    except ValueError:
        raise ValueError(f"Invalid input: {raw}")

