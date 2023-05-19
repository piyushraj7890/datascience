from rearrange import rearrange_name
import unittest


class TestRearrange(unittest.TestCase):
    def test_basic(self):
        testcase = "Raj, Piyush"
        expected = "Piyush Raj"
        self.assertEqual(rearrange_name(testcase), expected)

    def test_empty(self):
        testcase = ""
        expected = ""
        self.assertEqual(rearrange_name(testcase), expected)

    def test_double_name(self):
        testcase = "Hopper, Grace M."
        expected = "Grace M. Hopper"
        self.assertEqual(rearrange_name(testcase), expected)

    def test_one(self):
        testcase = "Piyush"
        expected = "Piyush"
        self.assertEqual(rearrange_name(testcase), expected)


unittest.main()
