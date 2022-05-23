import unittest
import sys
sys.path.insert(0, '..')

from stats.stats import DataCapture

class TestStatsAdd(unittest.TestCase):
    capture = DataCapture()

    def test_pass(self):
        self.assertEqual(self.capture.add(3), None)

    def test_fail(self):
        self.assertNotEqual(self.capture.add(3), 5)


class TestStatsLess(unittest.TestCase):
    capture = DataCapture()
    capture.add(3)
    capture.add(9)
    capture.add(3)
    capture.add(4)
    capture.add(6)
    stats = capture.build_stats()

    def test_pass(self):
        self.assertEqual(self.stats.less(4), 2)

    def test_fail(self):
        self.assertNotEqual(self.stats.less(5), 4)

    def test_error_int(self):
        with self.assertRaisesRegex(Exception, 'The value must be an integer'):
            self.stats.less(4.2)

    def test_error_range(self):
        with self.assertRaisesRegex(Exception, 'The value must be between 1 and 999'):
            self.stats.less(0)

        with self.assertRaisesRegex(Exception, 'The value must be between 1 and 999'):
            self.stats.less(1002)


class TestStatsBetween(unittest.TestCase):
    capture = DataCapture()
    capture.add(1)
    capture.add(2)
    capture.add(5)
    capture.add(6)
    capture.add(10)
    capture.add(2)
    capture.add(4)
    capture.add(7)
    capture.add(8)
    capture.add(3)
    capture.add(19)
    stats = capture.build_stats()

    def test_pass(self):
        self.assertEqual(self.stats.between(1, 5), 6)

    def test_fail(self):
        self.assertNotEqual(self.stats.between(1, 10), 11)

    def test_error_int(self):
        with self.assertRaisesRegex(Exception, 'The value must be an integer'):
            self.stats.between(34.50, 2)

    def test_error_range(self):
        with self.assertRaisesRegex(Exception, 'The value must be between 1 and 999'):
            self.stats.between(2, -2)

        with self.assertRaisesRegex(Exception, 'The value must be between 1 and 999'):
            self.stats.between(9999, 2)

    def test_error_end(self):
        with self.assertRaisesRegex(Exception, 'The end must be greater than or equal to start'):
            self.stats.between(6, 5)


class TestStatsGreater(unittest.TestCase):
    capture = DataCapture()
    capture.add(10)
    capture.add(20)
    capture.add(35)
    stats = capture.build_stats()

    def test_pass(self):
        self.assertEqual(self.stats.greater(20), 1)

    def test_fail(self):
        self.assertNotEqual(self.stats.greater(29), 2)

    def test_error_int(self):
        with self.assertRaisesRegex(Exception, 'The value must be an integer'):
            self.stats.greater(5.9)

    def test_error_range(self):
        with self.assertRaisesRegex(Exception, 'The value must be between 1 and 999'):
            self.stats.greater(-2)

        with self.assertRaisesRegex(Exception, 'The value must be between 1 and 999'):
            self.stats.greater(2050)
