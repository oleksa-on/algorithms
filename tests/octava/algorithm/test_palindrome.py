from unittest import TestCase
from src.octava.algorithm.palindrome import palindrome_string_what_to_delete

class Test(TestCase):
    # a => (nothing) => a
    def test_analyze_what_to_delete(self):
        self.assertEqual(0, palindrome_string_what_to_delete("a"))

    # abadc => (nothing) => abcba
    def test_analyze_what_to_delete_01(self):
        self.assertEqual(0, palindrome_string_what_to_delete("ababc"))

    # aaadaaa => (nothing) => aaadaaa
    def test_analyze_what_to_delete_02(self):
        self.assertEqual(0, palindrome_string_what_to_delete("aaadaaa"))

    # ab => (remove: b) => a
    def test_analyze_what_to_delete_03(self):
        self.assertEqual(1, palindrome_string_what_to_delete("ab"))

    # abcdef => (remove: b,c,d,e,f) => a
    def test_analyze_what_to_delete_04(self):
        self.assertEqual(5, palindrome_string_what_to_delete("abcdef"))

    # abcdef => (remove: a,b) => abdddba
    def test_analyze_what_to_delete_05(self):
        self.assertEqual(2, palindrome_string_what_to_delete("aaabbbddd"))

    # xxxyyyxxx => (remove: nothing) => xxxyyyxxx
    def test_analyze_what_to_delete_06(self):
        self.assertEqual(0, palindrome_string_what_to_delete("xxxyyyxxx"))