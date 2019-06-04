import unittest
from main import calculate


class TestCalculations(unittest.TestCase):
    """Class for testing various use cases of calculate()"""

    # test empty meme list
    def test_empty_list(self):
        self.assertEqual(calculate(1, []), (0, set()))

    # test 0 capacity usb stick
    def test_empty_usb_stick(self):
        self.assertEqual(calculate(0, [
            ('rollsafe.jpg', 205, 6),
            ('sad_pepe_compilation.gif', 410, 10),
            ('yodeling_kid.avi', 605, 12)
        ]), (0, set()))

    # test of 0 capacity usb stick and empty meme array
    def test_empty_usb_stick_and_list(self):
        self.assertEqual(calculate(0, []), (0, set()))
