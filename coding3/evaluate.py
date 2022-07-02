import unittest
import exercise

j = complex(0, 1)
TESTDATA = [
    ([1, -2, 3, -4], [-2, -2-2*j, 10, -2+2*j]),
]

class Evaluate(unittest.TestCase):
    def test_exercise(self):
        for seq, expected in TESTDATA:
            results = exercise.ComputeDFT(seq)
            self.assertIsInstance(results, list)
            self.assertEqual(len(expected), len(results))
            for x, y in zip(expected, results):
                self.assertAlmostEqual(x, y, delta=0.01)

if __name__ == '__main__':
    unittest.main()