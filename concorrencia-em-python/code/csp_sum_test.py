import unittest

import csp.csp as csp

import csp_sum


class SumTestCase(unittest.TestCase):

    def test_sum_odd_integers_from_start_to_end(self):
        ch = csp.Channel()
        proc = csp_sum.sum(ch, 1, 10)
        proc.start()
        self.assertEqual(25, ch.read())

unittest.main()
