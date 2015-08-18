import unittest

from lcoj.reverse_int import reverse


class TestReverseInt(unittest.TestCase):

    def test_reverse_single_digit_positive(self):
        self.assertEqual(reverse(None, 5), 5)

    def test_reverse_multiple_digit_positive(self):
        self.assertEqual(reverse(None, 53), 35)

    def test_reverse_single_digit_negative(self):
        self.assertEqual(reverse(None, -5), -5)

    def test_reverse_multiple_digit_negative(self):
        self.assertEqual(reverse(None, -53), -35)

    def test_reverse_multiple_digit_positive_zero(self):
        self.assertEqual(reverse(None, 130), 31)

    def test_reverse_multiple_digit_negative_zero(self):
        self.assertEqual(reverse(None, -130), -31)

    def test_too_big_when_reversed(self):
        self.assertEqual(reverse(None, 1147483647), 0)

    def test_too_big_when_reversed_negative(self):
        self.assertEqual(reverse(None, -1147483647), 0)
