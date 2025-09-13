import numpy as np

# A = np.array([1, 3],
#              [3, 4])

#   = np.array([1, 2])

# Tx = A @  
# print(f"array = {Tx}")

# kx, ky = 2, 3
# A = np.array([[kx, 3],
#              [3, ky]])

# x = np.array([4, 5])

# Tx = A @ x
# print(f"Original Vector = {x}")
# print(f"Sacled Vector = {Tx}")

# theta = np.pi / 2 #90 degree rotate

# A = np.array([[np.cos(theta), -np.sin(theta)],
#               [np.sin(theta), np.cos(theta)]])

# x = np.array([3,2])
# rotated_vector = A @ x
# print(f"Original Vector = {x}")
# print(f"Rotated Vector = {rotated_vector}")

# A = np.array([[1, 0],
#               [0, -1]])#reflected on x axis
# x = np.array([4, 5])
# reflected_vector = A @ x
# print(f"Original Vector = {x}")
# print(f"Reflected Vector = {reflected_vector}")

# A = np.array([[-1, 0],
#               [0, 1]])#reflected on y axis
# x = np.array([4, 5])
# reflected_vector = A @ x
# print(f"Original Vector = {x}")
# print(f"Reflected Vector = {reflected_vector}")

A = np.array([[-1, 0],
             [4, 9]])
B = np.array([[4, 7],
             [4, 10]])

x = np.array([1, 2])

result1 = B @ (A @ x)

intermediate_matrix = B @ A # B @ (A @x) = (B @ A) @  

result2 = intermediate_matrix

print(result1)
print(result2)

