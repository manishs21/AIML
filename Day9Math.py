import numpy as np # numpy -> np
import scipy.linalg as la

# #Vector
# v = np.array([1, 2, 3])
# print(v)


# #Matrix
# A = np.array([[1, 2], [3, 4]]) 
# '''
# 1   2
# 3   4 - > 2 x 2
# '''
# print(A)

# Scalar Multiplication

# v_scaled = 8 * v
# print(v_scaled)

# A = np.array([[1, 2], [3, 4]])

# B = np.array([2, 4])

# C = A @ B
# print(C)

# add_v = A + B
# print(add_v)

# A_Transpose = A.T
# print(A_Transpose)

# 2x + 3y = 8, 5x = 4y = 13
# b = [8, 13]
# A = 2 3
#     5 4
# A = np.array([2, 3], [5, 4])
# b = np.array([8, 13])
# x = np.linalg.solve(A, b)
# print(f"Solution = {x}")

# A = np.array([[2, 3], [5, 4]])
# b = np.array([8, 13])
# x = np.linalg.solve(A, b)
# print(f"Solution = {x}")

# A = np.array([[8, 3, -2], [4, 7, 5], [3, 4, -12] ])
# b = np.array([9, 15, 35])
# x = np.linalg.solve(A, b)
# print(f"Solution = {x}")

# A = np.array([[2, 4, 5],
#               [1, 3, 2],
#               [4, 2, 1]])

# P, L, U = la.lu(A) 
# print(P)
# print(L)
# print(U)

# # P X A = L X U

#QR is for Rectangle matrix or others
A = np.array([[1, 2, 3],
             [3, 4, 5]])
Q, R = np.linalg.qr(A)
result = Q @ R
print(A)
print(result)



