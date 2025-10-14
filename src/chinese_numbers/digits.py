# Digit and unit character sets for Traditional and Simplified Chinese numerals

TRADITIONAL_DIGITS = {0: '零', 1: '一', 2: '二', 3: '三', 4: '四', 5: '五', 6: '六', 7: '七', 8: '八', 9: '九'}
SIMPLIFIED_DIGITS = {0: '零', 1: '一', 2: '二', 3: '三', 4: '四', 5: '五', 6: '六', 7: '七', 8: '八', 9: '九'}

TRADITIONAL_UNITS = ['', '十', '百', '千']
SIMPLIFIED_UNITS = ['', '十', '百', '千']

TRADITIONAL_BIG_UNITS = ['', '萬', '億', '兆', '京', '垓', '秭', '穰', '溝', '澗', '正', '載']
SIMPLIFIED_BIG_UNITS = ['', '万', '亿', '兆', '京', '垓', '秭', '穰', '沟', '涧', '正', '载']

def get_digits(traditional=True):
    return TRADITIONAL_DIGITS if traditional else SIMPLIFIED_DIGITS

def get_units(traditional=True):
    return TRADITIONAL_UNITS if traditional else SIMPLIFIED_UNITS

def get_big_units(traditional=True):
    return TRADITIONAL_BIG_UNITS if traditional else SIMPLIFIED_BIG_UNITS
