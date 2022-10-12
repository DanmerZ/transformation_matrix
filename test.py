import unittest
import numpy as np

from transformation_matrix import calculate_transformation_matrix

class TestTransformation(unittest.TestCase):
    def test_calculate_transformation_matrix(self):
        """
        Calculate transformation matrix for 6 pairs of points
        from two coordinate frames A and B
        """

        # Expected transformation matrix
        T_a_b_expected = np.array(
            [[0.3830,  0.3214, -0.8660, 3.0],
            [-0.4492, 0.8840,  0.1294, 7.0],
            [0.8072,  0.3394,  0.4830, 1.0],
            [0.0,     0.0,     0.0,    1.0]]
        )

        # points of A coordinate frame 
        pa_1 = np.array([0.5449, 0.1955, 0.9227, 1.0])
        pa_2 = np.array([0.6862, 0.7202, 0.8004, 1.0])
        pa_3 = np.array([0.8936, 0.7218, 0.2859, 1.0])
        pa_4 = np.array([0.0548, 0.8778, 0.5437, 1.0])
        pa_5 = np.array([0.3037, 0.5824, 0.9848, 1.0])
        pa_6 = np.array([0.0462, 0.0707, 0.7157, 1.0])

        # points in B frame based on expected transformation
        pb_1 = T_a_b_expected @ pa_1
        pb_2 = T_a_b_expected @ pa_2
        pb_3 = T_a_b_expected @ pa_3
        pb_4 = T_a_b_expected @ pa_4
        pb_5 = T_a_b_expected @ pa_5
        pb_6 = T_a_b_expected @ pa_6

        points_a = [pa_1, pa_2, pa_3, pa_4, pa_5, pa_6]
        points_b = [pb_1, pb_2, pb_3, pb_4, pb_5, pb_6]

        T_a_b = calculate_transformation_matrix(points_a, points_b)

        self.assertTrue(np.allclose(T_a_b, T_a_b_expected))

if __name__ == '__main__':
    unittest.main()