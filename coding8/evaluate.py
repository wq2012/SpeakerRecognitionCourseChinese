import unittest
import exercise


TESTDATA = [
    ([1, -2, 3], [0.11849965453500957, 0.005899750401902781, 0.8756005950630876]),
    ([0, 0, 0], [0.3333333333333333, 0.3333333333333333, 0.3333333333333333]),
    ([-0.1, 0.2], [0.42555748318834097, 0.574442516811659]),
    ([999, -999, 999], [0.5, 0.0, 0.5]),
    ([2, 2, 3, 4, -1], [0.08225629006438344, 0.08225629006438344, 0.2235957785584698, 0.607796341775641, 0.004095299537122306]),
]
class Evaluate(unittest.TestCase):
    def test_exercise(self):
        for vec, expected in TESTDATA:
          result = exercise.ComputeSoftmax(vec)
          self.assertEqual(len(result), len(expected))
          for x, y in zip(result, expected):
            self.assertAlmostEqual(x, y, delta=0.0001)

if __name__ == '__main__':
    unittest.main()