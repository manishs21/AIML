import numpy as np
import scipy.linalg as la

# v = np.array([1, 2, 3])
# print(v)

# mat = np.array([[1,2,3],
#                 [4,5,6],
#                 [7,8,9]])
# new_v = 4 * v
# print(new_v)


mat1 = np.array([[1,2,3],
                [4,5,6],
                [7,8,9]])


mat2 = np.array([[5,7,8],
                [4,5,6],
                [7,8,9]])
# add_mat = mat1 + mat2   #addition
# print(add_mat)

# sub_mat = mat1 - mat2  #substract
# print(sub_mat)

# t_mat1 = mat1.T   #Transpose row to column
# print(t_mat1)

# mul_mat = mat1 @ mat2   #multiply
# print(mul_mat)

# det1 = np.linalg.det(mat1)  #determinant yo * yo sing change yo * yo
# det2 = np.linalg.det(mat2)
# print(det1)
# print(det2)

# inv_mat2 = np.linalg.inv(mat2)  #inverse of matrix
# print(inv_mat2)


# 2x + 3y = 8  # solving this equation
# 5x + 4y = 13
# A = np.array([[2, 3], [5, 4]])
# b = np.array([8, 13])

# cal = np.linalg.solve(A, b)
# print(cal)

# A = np.array([[8, 3, -2], [-4, 7, 5], [3, 5, 3]])
# b = np.array([9, 15, 35])

# cal = np.linalg.solve(A, b)
# print(cal)


# A = np.array([[2,4,5],
#               [1,3,2],
#               [4,2,1]])
# P, L, U = la.lu(A)
# print(P)
# print(L)
# print(U)


# kx, ky = 2, 5
# A = np.array([[kx, 0],
#               [0, ky]])
# x = np.array([4,5])
# T_s = A @ x
# print(x)
# print(T_s)

# theta = np.pi / 4
# A = np.array([[np.cos(theta), -np.sin(theta)],
#               [np.sin(theta), np.cos(theta)]])

# x = np.array([5,6])

# t = A @ x
# print(x)
# print(t)


# Ax = np.array([[1, 0],
#               [0, -1]])

# Ay = np.array([[-1, 0],
#               [0, 1]])

# x = np.array([4, 3])
# ref_x = Ax @ x
# ref_y = Ay @ x
# print(ref_x)
# print(ref_y)



