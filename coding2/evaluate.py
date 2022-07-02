import unittest
import exercise


TESTDATA = [
    ([1, 2], 0),
    ([-2, -1], 0),
    ([-2, 1], 1),
    ([-1, 1, -1, 1, -1, 1], 5),
    ([2, 1, 3, 1, 5, 4], 0),
    ([-0.2, -0.1, -0.3, -0.1, -0.5, -0.4], 0),
    ([-0.2, 0.1, 0.3, -0.1, -0.5, -0.4, 12, 15, -23], 4),
]


class Evaluate(unittest.TestCase):
    def test_exercise(self):
        for signal, expected in TESTDATA:
            result = exercise.ComputeZeroCross(signal)
            self.assertEqual(expected, result)

if __name__ == '__main__':
    unittest.main()