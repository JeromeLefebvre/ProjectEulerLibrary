from bisect import bisect_left, bisect_right


class Orderedlist:
    def __init__(self, ordered=[]):
        self.ordered = ordered

    def indexAbove(self, x):
        try:
            i = bisect_left(self.ordered, x)
            return i
        except IndexError:  # We've hit an element above everything
            return -1

    def indexBelow(self, x):
        '''Returns the index of the largest or equal element below'''
        try:
            i = bisect_right(self.ordered, x)
            return i-1
        except IndexError:  # We've hit an element above everything
            return -1

    def __contains__(self, x):
        i = bisect_left(self.ordered, x)
        if i != len(self.ordered) and self.ordered[i] == x:
            return i
        raise ValueError

    def __getitem__(self, pos):
        start, stop = pos.start, pos.stop
        if start > stop:
            return ()
        return self.ordered[self.indexAbove(start):self.indexBelow(stop)+1]

    def __str__(self):
        return str(self.ordered)

    def __repr__(self):
        return "Orderedlist(" + str(self.ordered) + ")"

    def __eq__(self, other):
        if not isintance(other, Orderedlist):
            return False
        return self.ordered == other.ordered

import unittest


class TestOrdered(unittest.TestCase):
    def test_ordered(self):
        m = (-1, 2, 3, 4, 10, 33, 141)
        l = Orderedlist(m)
        self.assertEqual(m[l.indexBelow(2)], 2)
        self.assertEqual(m[l.indexBelow(15)], 10)
        self.assertEqual(m[l.indexBelow(3)], 3)
        self.assertEqual(m[l.indexBelow(2200)], 141)
        self.assertEqual(m[l.indexAbove(4)], 4)
        self.assertEqual(m[l.indexAbove(10)], 10)
        self.assertEqual(m[l.indexAbove(1)], 2)
        self.assertEqual(m[l.indexAbove(5)], 10)
        self.assertEqual(m[l.indexAbove(4)], 4)
        self.assertEqual(m[l.indexAbove(2)], 2)
        self.assertEqual(m[l.indexAbove(140)], 141)
        self.assertEqual(m[l.indexAbove(0)], 2)
        self.assertEqual(m[l.indexAbove(-5)], -1)
        self.assertEqual(m[l.indexAbove(3)], 3)
        self.assertEqual(l[3:4], (3, 4))
        self.assertEqual(l[5:11], (10,))
        self.assertEqual(l[4:11], (4, 10))
        self.assertEqual(l[1:11], (2, 3, 4, 10))
        self.assertEqual(l[11:1], ())
        m = (2, 3, 5)
        l = Orderedlist(m)
        self.assertEqual(l[1:100], (2, 3, 5))
        self.assertEqual(l[3:100], (3, 5))

    def test_badContainer(self):
        m = (10, 15)
        l = Orderedlist(m)
        self.assertEqual(l.indexAbove(1), 0)
        self.assertEqual(l.indexAbove(10), 0)
        self.assertEqual(l.indexAbove(15), 1)
        self.assertEqual(l.indexAbove(20), 2)

    def test_containment(self):
        from PE_primes import primesUpTo
        m = Orderedlist(primesUpTo(1000))
        self.assertTrue(101 in m)
        self.assertRaises(ValueError, lambda x: x in m, 100)

    def test_print(self):
        m = (-1, 2, 3, 4, 10, 33, 141)
        l = Orderedlist(m)
        self.assertTrue(str(l), str(m))

    def test_repr(self):
        m = (-1, 2, 3, 4, 10, 33, 141)
        l = Orderedlist(m)
        self.assertTrue(eval(repr(l)), l)

if __name__ == "__main__":
    unittest.main()
