import unittest
import exercise

class Evaluate(unittest.TestCase):
    def test_exercise(self):
        eer = exercise.ComputeEER()
        self.assertGreaterEqual(eer, 0.08125)
        self.assertLessEqual(eer, 0.1)

if __name__ == '__main__':
    unittest.main()