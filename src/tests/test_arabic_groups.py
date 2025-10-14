"""
there are only 2 idiomatic overrides - as seen here:

Input Number: 123456789
  Grouped Digits: ['1', '2345', '6789']
  No Idiomatic Override

Input Number: 1001
  Grouped Digits: ['1001']
  No Idiomatic Override

Input Number: 42
  Grouped Digits: ['42']
  No Idiomatic Override

Input Number: 10000000000000000
  Grouped Digits: ['1', '0000', '0000', '0000', '0000']
  Idiomatic Override: 一千萬億

Input Number: 100000000000000000
  Grouped Digits: ['10', '0000', '0000', '0000', '0000']
  Idiomatic Override: 一京

Input Number: 100000000
  Grouped Digits: ['1', '0000', '0000']
  No Idiomatic Override

Input Number: 1000000000000
  Grouped Digits: ['1', '0000', '0000', '0000']
  No Idiomatic Override

Input Number: 0 
  Grouped Digits: ['0']
  No Idiomatic Override
"""

from chinese_numbers.arabic import ArabicNumber

def test_arabic_number_groupings():
  cases = [
    # (input, expected_groups, expected_idiom, reason)
    ("0", ["0"], None, "Zero"),
    ("10", ["10"], None, "Ten"),
    ("11", ["11"], None, "Eleven"),
    ("20", ["20"], None, "Twenty"),
    ("101", ["101"], None, "Hundred with trailing one"),
    ("1001", ["1001"], None, "Thousand with trailing one"),
    ("10000", ["1", "0000"], None, "Ten thousand"),
    ("10001", ["1", "0001"], None, "Ten thousand and one"),
    ("10010", ["1", "0010"], None, "Ten thousand and ten"),
    ("1000000", ["100", "0000"], None, "Million"),
    ("100000000", ["1", "0000", "0000"], None, "Hundred million"),
    ("1000000000000", ["1", "0000", "0000", "0000"], None, "Trillion"),
    ("10000000000000000", ["1", "0000", "0000", "0000", "0000"], "一千萬億", "One thousand trillion (idiomatic)"),
    ("1234567890", ["12", "3456", "7890"], None, "Full span"),
    ("10 0000 0001", ["10", "0000", "0001"], None, "Billion and one"),
    ("1 0010 0010", ["1", "0010", "0010"], None, "Multiple zeros"),
    ("10 0000 0000 0000 0000", ["10", "0000", "0000", "0000", "0000"], "一京", "One hundred quadrillion (京)"),
    ("100 0000 0000 0000 0000", ["100", "0000", "0000", "0000", "0000"], None, "One hundred quadrillion without idiom"),
    ("123 4567 8901 2345 6789", ["123", "4567", "8901", "2345", "6789"], None, "Very large number with all groups"),
  ]
  for num, expected, expected_idiom, reason in cases:
    a = ArabicNumber(num)
    try:
      assert a.groups == expected, f"{num}: {a.groups} != {expected} ({reason})"
      idiom = a.get_idiomatic_override()
      assert idiom == expected_idiom, f"{num}: idiom {idiom} != {expected_idiom} ({reason})"
      print(f"Passed: {num} -> {a.groups} [idiom: {idiom}] [{reason}]")
    except AssertionError as e:
      print(f"FAILED: {num}\n  Actual groups: {a.groups}\n  Expected groups: {expected}\n  Actual idiom: {a.get_idiomatic_override()}\n  Expected idiom: {expected_idiom}\n  Reason: {reason}")
      raise
