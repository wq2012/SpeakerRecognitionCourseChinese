import unittest
import exercise


TESTDATA = [
    ([0, 1], [0.2, 0.8], 0.2231435513142097),
    ([0, 1, 0], [0.1, 0.6, 0.3], 0.5108256237659907),
    ([0, 1, 0, 0, 0], [0.1, 0.6, 0.1, 0.2, 0], 0.5108256237659907),
    ([0, 0, 1, 0, 0, 0], [0.1, 0.05, 0.55, 0.1, 0.2, 0], 0.5978370007556204),
]
class Evaluate(unittest.TestCase):
    def test_exercise(self):
        for p, q, ce in TESTDATA:
          result = exercise.ComputeCrossEntropy(p, q)
          self.assertAlmostEqual(ce, result, delta=0.01)

    def test_logzero(self):
        p, q = ([0, 1, 0], [0.2, 0, 0.8])
        result = exercise.ComputeCrossEntropy(p, q)
        self.assertGreater(result, 3)

if __name__ == '__main__':
    unittest.main()