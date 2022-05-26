import unittest
import exercise

TESTDATA = [
    (1000, 1000),
    (10, 15.99),
    (100, 150.49),
    (700, 781.18),
    (10000, 3073.24),
    (500, 607.45),
    (16000, 3574.94),
]

class Evaluate(unittest.TestCase):
    def test_exercise(self):
        for freq, expected in TESTDATA:
            result = exercise.FrequencyToMel(freq)
            self.assertAlmostEqual(expected, result, delta=0.1)

if __name__ == '__main__':
    unittest.main()