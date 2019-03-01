import unittest
def min(l):
    # Should find and return minimum value in a given list
    min = l[0]
    for val in l:
        if val < min:
            min = val
    return min
def sum_list(l):
    # Should return total value of all list items
    total = 0
    for val in l:
        total += val
    return total
def less_than(a):
    # Should return a bool of whether given value is less than 100
    return a < 100

class MainTest(unittest.TestCase):
    def test_min(self):
        self.assertEqual(min([4, 2, 9]), 2)
        self.assertEqual(min([3, -2, 200]), -2)
        self.assertEqual(min([0, 0, 4, 5, 9]), 0)
    def test_sum_list(self):
        self.assertEqual(sum_list([1, 6, 5]), 12)
        self.assertEqual(sum_list([-4, 100]), 96)
        self.assertEqual(sum_list([-1, -3, -3, -1]), -8)
    def test_less_than(self):
        self.assertTrue(less_than(4))
        self.assertTrue(less_than(-2))
        self.assertTrue(less_than(0))