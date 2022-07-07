import unittest
import exercise


TESTDATA = [
    ([1, 2], [2, 1], [[4, 3], [3, 4]], -3.1114),
    ([2, -1], [-3, 2], [[-4, 3], [-3, 4]], -1.1880),
    ([1, 2, 1], [1, 1, 1], [[4, 3, -2], [-3, 4, -1]], 3.3501),
]


class Evaluate(unittest.TestCase):
    def test_exercise(self):
        for test_vec, enroll_vec, cohort_vecs, expected in TESTDATA:
            result = exercise.ComputeTNormScore(
                test_vec, enroll_vec, cohort_vecs)
            self.assertAlmostEqual(expected, result, delta=0.01)

if __name__ == '__main__':
    unittest.main()