import unittest
import exercise

TESTDATA = [
    ([1, 1], [1, 1], 1),
    ([1, 1], [-1, -1], -1),
    ([1, 1], [-1, 1], 0),
    ([0.1, 0.2], [0.3, 0.4], 0.98387),
    ([1, 1, 1], [0.2, -0.4, 0.6], 0.30860),
    ([-0.22, 0.56, 0.73, 0.44], [0, 0.3, -0.2, 3.3],  0.42559),
    ]

class Evaluate(unittest.TestCase):
    def test_exercise(self):
        for vec1, vec2, expected in TESTDATA:
            self.assertAlmostEqual(exercise.ComputeCosine(vec1, vec2), expected, delta=0.00001)

if __name__ == '__main__':
    unittest.main()