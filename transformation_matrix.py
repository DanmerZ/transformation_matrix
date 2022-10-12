# Based on "Automatic Calculation of a Transformation Matrix Between Two Frames"
# by JASMINE CASHBAUGH, CHRISTOPHER KITTS
# DOI 10.1109/ACCESS.2018.2799173
# https://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=8271986ß

import numpy as np

def calculate_A(points):
    """
    Matrix A defined by formula 11 in the paper
    """
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
    """
    Vectors on the right hand sides of formulae 10, 12 and 13 in the paper
    """
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
    """
    Compose transformation matrix from the corresponding matrix elements 
    defined by formulae 10, 12, 13 
    """
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

