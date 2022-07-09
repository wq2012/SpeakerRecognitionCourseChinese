import unittest
import exercise

TESTDATA = [
    ([1, 2, 3, 4], [1, -1], [-1, -1, -1]),
    ([1, 2, 4, 5, -2], [1, 1], [3, 6, 9, 3]),
    ([1, 2, 4, 5, -2], [1, 1, 1], [7, 11, 7]),
    ([0, 0, 0, 0, 0], [1, 1, 1, 1], [0, 0]),
    ([1, 1, -1, -1, -1], [0, 0, 0, 0], [0, 0]),
]

class Evaluate(unittest.TestCase):
    def test_exercise(self):
        for seq, kernel, expected in TESTDATA:
            result = exercise.ComputeConvolution(seq, kernel)
            self.assertIsInstance(result, list)
            self.assertListEqual(expected, result)


if __name__ == '__main__':
    unittest.main()