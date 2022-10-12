from re import X
import numpy as np

T_a_b = np.array(
    [[0.3830,  0.3214, -0.8660, 3.0],
     [-0.4492, 0.8840,  0.1294, 7.0],
     [0.8072,  0.3394,  0.4830, 1.0],
     [0.0,     0.0,     0.0,    1.0]])

T_b_a = np.linalg.inv(T_a_b)

pa_1 = np.array([0.5449, 0.1955, 0.9227, 1.0])
pa_2 = np.array([0.6862, 0.7202, 0.8004, 1.0])
pa_3 = np.array([0.8936, 0.7218, 0.2859, 1.0])
pa_4 = np.array([0.0548, 0.8778, 0.5437, 1.0])
pa_5 = np.array([0.3037, 0.5824, 0.9848, 1.0])
pa_6 = np.array([0.0462, 0.0707, 0.7157, 1.0])

pb_1 = np.array([2.5144, 7.0691, 1.9754, 1.0])
pb_2 = np.array([2.8292, 7.4454, 2.2224, 1.0])
pb_3 = np.array([3.3518, 7.3060, 2.1198, 1.0])
pb_4 = np.array([2.8392, 7.8455, 1.6229, 1.0])
pb_5 = np.array([2.4901, 7.5449, 1.9518, 1.0])
pb_6 = np.array([2.4273, 7.1354, 1.4349, 1.0])

points_a = [pa_1, pa_2, pa_3, pa_4, pa_5, pa_6]
points_b = [pb_1, pb_2, pb_3, pb_4, pb_5, pb_6]

def calculate_A(points):
    A = np.zeros((4, 4))
    
    for p in points:
        x_a, y_a, z_a, _ = p

        A[0][0] += x_a * x_a
        A[0][1] += x_a * y_a
        A[0][2] += x_a * z_a
        A[0][3] += x_a

        A[1][0] += x_a * y_a
        A[1][1] += y_a * y_a
        A[1][2] += y_a * z_a
        A[1][3] += y_a

        A[2][0] += x_a * z_a
        A[2][1] += y_a * z_a
        A[2][2] += z_a * z_a
        A[2][3] += z_a

        A[3][0] += x_a
        A[3][1] += y_a
        A[3][2] += z_a
    
    A[3][3] = len(points)

    return A

def calcualate_V(points_a, points_b):
    Vx = np.zeros((4))
    Vy = np.zeros((4))
    Vz = np.zeros((4))

    for i in range(len(points_a)):
        x_a, y_a, z_a, _ = points_a[i]
        x_b, y_b, z_b, _ = points_b[i]
        
        Vx[0] += x_b * x_a
        Vx[1] += x_b * y_a
        Vx[2] += x_b * z_a
        Vx[3] += x_b

        Vy[0] += y_b * x_a
        Vy[1] += y_b * y_a
        Vy[2] += y_b * z_a
        Vy[3] += y_b 

        Vz[0] += z_b * x_a
        Vz[1] += z_b * y_a
        Vz[2] += z_b * z_a
        Vz[3] += z_b 

    return (Vx, Vy, Vz)

def calculate_transformation_matrix(points_a, points_b):
    A = calculate_A(points_a)
    A_inv = np.linalg.inv(A)
    Vx, Vy, Vz = calcualate_V(points_a, points_b)

    rxx, rxy, rxz, tx = A_inv @ Vx
    ryx, ryy, ryz, ty = A_inv @ Vy
    rzx, rzy, rzz, tz = A_inv @ Vz

    A_calc = np.array([
        [rxx, rxy, rxz, tx],
        [ryx, ryy, ryz, ty],
        [rzx, rzy, rzz, tz],
        [0, 0, 0, 1]
    ])

    return A_calc

A_calc = calculate_transformation_matrix(points_a, points_b)
print(A_calc)


# p2 = A @ p1

# p1_c = A_inv @ p2

# print(p2)
# print(p1_c)