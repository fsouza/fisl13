import unittest

import local_sum


class LocalSumTestCase(unittest.TestCase):

    def setUp(self):
        local_sum.total = 0

    def test_should_sum_odd_numbers_from_begin_to_end(self):
        t = local_sum.LocalSum(start=1, end=10)
        t.start()
        t.join()
        self.assertEqual(local_sum.total, 25)

unittest.main()
