import unittest
from range_glob import glob_for_range


class GlobForRangeTest(unittest.TestCase):

    def test_quality(self):
        self.assertEqual(glob_for_range(1, 1), '1')
        self.assertEqual(glob_for_range(0, 1), '[0-1]')
        self.assertEqual(glob_for_range(0, 2), '[0-2]')
        self.assertEqual(glob_for_range(65666, 65667), '6566[6-7]')
        self.assertEqual(glob_for_range(12, 3456), r'{1[2-9],[2-9][0-9],[1-9][0-9][0-9],[1-2][0-9][0-9][0-9],3[0-3][0-9][0-9],34[0-4][0-9],345[0-6]}')
        self.assertEqual(glob_for_range(1, 19), r'{[1-9],1[0-9]}')
        self.assertEqual(glob_for_range(1, 99), r'{[1-9],[1-9][0-9]}')


if __name__ == '__main__':
    unittest.main()
