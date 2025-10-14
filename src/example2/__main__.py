
"""
Minimal example: How to use ChineseNumberConverter from chinese_numbers.

Shows the simplest way to import, instantiate, and use the converter.
"""

from chinese_numbers.converter import ChineseNumberConverter


def main():
    """
    Basic usage: Convert a number to Chinese numerals.
    """
    converter = ChineseNumberConverter(use_traditional=False)  # Simplified by default
    number = "12345"
    result = converter.convert(number)
    print(f"{number} -> {result}")


if __name__ == "__main__":
    main()
