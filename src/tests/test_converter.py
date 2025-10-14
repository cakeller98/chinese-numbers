from chinese_numbers.converter import ChineseNumberConverter

def test_chinese_number_converter():
    converter_trad = ChineseNumberConverter(use_traditional=True)
    converter_simp = ChineseNumberConverter(use_traditional=False)
    cases = [
        # (input, expected_trad, expected_simp, reason)
        ("0", "零", "零", "Zero"),
        ("10", "十", "十", "Omit leading 一 for 十"),
        ("11", "十一", "十一", "十一 idiomatic"),
        ("20", "二十", "二十", "Tens"),
        ("101", "一百零一", "一百零一", "Internal zero"),
        ("1001", "一千零一", "一千零一", "Internal zero"),
        ("10000", "一萬", "一万", "First big unit"),
        ("10001", "一萬零一", "一万零一", "萬 with trailing digits"),
        ("10010", "一萬零一十", "一万零一十", "萬 with internal zero"),
        ("1000000", "一百萬", "一百万", "百萬"),
        ("100000000", "一億", "一亿", "億/亿"),
        ("1000000000000", "一兆", "一兆", "兆"),
        ("10000000000000000", "一千萬億", "一千万亿", "Ultra-large idiomatic override"),
        ("123456789", "一億二千三百四十五萬六千七百八十九", "一亿二千三百四十五万六千七百八十九", "Full span"),
        ("1000000001", "十億零一", "十亿零一", "Zero after big unit"),
        ("100100010", "一億零一十萬零一十", "一亿零一十万零一十", "Multiple zeros"),
        ("100000000000000000", "一京", "一京", "京"),
    ]
    for num, exp_trad, exp_simp, reason in cases:
        out_trad = converter_trad.convert(num)
        out_simp = converter_simp.convert(num)
        assert out_trad == exp_trad, f"[Traditional] {num}: {out_trad} != {exp_trad} ({reason})"
        assert out_simp == exp_simp, f"[Simplified] {num}: {out_simp} != {exp_simp} ({reason})"
        print(f"Passed: {num} -> {out_trad} (trad), {out_simp} (simp) [{reason}]")

if __name__ == "__main__":
    test_chinese_number_converter()

