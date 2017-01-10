import unittest

from processing.main import main_func


class MainTest(unittest.TestCase):
    def test_main_func(self):
        self.assertEqual(main_func('hello'), 'olleh')


if __name__ == '__main__':
    unittest.main()
