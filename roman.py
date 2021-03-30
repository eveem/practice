import unittest
from nose.tools import assert_equals

def roman_converter(num):
    result = ""

    if num >= 1000:
        result += "M" * (num // 1000)
        num -= num // 1000 * 1000

    if num >= 900:
        result += "CM"
        num -= 900

    if num >= 500:
        result += "D" + ((num // 100 - 5) * "C")
        num -= num // 100 * 100

    if num >= 400:
        result += "CD"
        num -= 400

    if num >= 100:
        result += "C" * (num // 100)
        num -= num // 100 * 100

    if num >= 90:
        result += "XC"
        num -= 90

    if num >= 50:
        result += "L" + ((num // 10 - 5) * "X")
        num -= num // 10 * 10

    if num >= 40:
        result += "XL"
        num -= 40

    if num >= 10:
        result += "X" * (num // 10)
        num -= num // 10 * 10

    if num >= 9:
        result += "IX"
        num = 0

    if num >= 5:
        result += "V" + ((num - 5) * "I")
        num = 0

    if num >= 4:
        result += "IV"
        num = 0

    if num >= 1:
        result += "I" * num
        num = 0

    return result

class TestConverter(unittest.TestCase):
    def test_input_3000(self):
        assert_equals("MMM", roman_converter(3000))

    def test_input_3900(self):
        assert_equals("MMMCM", roman_converter(3900))

    def test_input_700(self):
        assert_equals("DCC", roman_converter(700))
    
    def test_input_500(self):
        assert_equals("D", roman_converter(500))
    
    def test_input_1500(self):
        assert_equals("MD", roman_converter(1500))

    def test_input_400(self):
        assert_equals("CD", roman_converter(400))

    def test_input_300(self):
        assert_equals("CCC", roman_converter(300))

    def test_input_1200(self):
        assert_equals("MCC", roman_converter(1200))

    def test_input_30(self):
        assert_equals("XXX", roman_converter(30))

    def test_input_280(self):
        assert_equals("CCLXXX", roman_converter(280))

    def test_input_1050(self):
        assert_equals("ML", roman_converter(1050))

    def test_input_15(self):
        assert_equals("XV", roman_converter(15))

    def test_input_1994(self):
        assert_equals("MCMXCIV", roman_converter(1994))

    def test_input_58(self):
        assert_equals("LVIII", roman_converter(58))

    def test_input_9(self):
        assert_equals("IX", roman_converter(9))

    def test_input_4(self):
        assert_equals("IV", roman_converter(4))