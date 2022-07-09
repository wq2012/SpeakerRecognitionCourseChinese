import unittest
import exercise

TESTDATA = [
    ([1, 2], [3, 1], [-2, -4], 1, 0),
    ([1, 2], [-2, -4], [3, 1], 1, 41),
    ([1, 2, 3], [4, 1, 2], [2, 1, 5], 1, 6),
    ([0, 0], [0, 0], [0, 0], 0, 0),
    ([0, 0], [0, 0], [0, 0], 1, 1),
    ([0, 0], [0, 0], [0, 0], 0.1, 0.1),
]

class Evaluate(unittest.TestCase):
    def test_exercise(self):
        for anchor, pos, neg, alpha, expected in TESTDATA:
            result = exercise.ComputeTripletLess(anchor, pos, neg, alpha)
            self.assertAlmostEqual(expected, result, delta=0.001)


if __name__ == '__main__':
    unittest.main()