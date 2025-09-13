#Broadcasting
import numpy as np

# arr = np.array([1, 2, 3, 4, 5]) # v
# s = 5

# new_arr = arr * s

# print(arr)
# print(new_arr)

# s = 4
# mat = np.array([[1, 2, 4],
#                 [2, 3, 5],
#                 [5, 7, 3]])

# new_mat = s - mat
# print(mat)
# print(new_mat)

# mat = np.array([[2, 4, 7],  #3x3 matrix
#                 [3, 4, 7],
#                 [4, 6, 9]])

# v = np.array([1, 2, 3])   #vector
# new_mat = mat + v
# print(mat)
# print(new_mat)

# a = np.array([5, 3, 1, 4, 7])
# print(np.sort(a))   #acending

# a = np.array([5, 3, 1, 4, 7])
# print(np.sort(a)[::-1])   #decending

# m = np.array([[4, 6, 9],
#               [2, 1, 8],
#               [7, 9, 1]])

# new_m = np.sort(m, axis = 1) # row sort
# print(m)
# print(new_m)

# new_m = np.sort(m, axis = 0) # column sort
# print(m)
# print(new_m)


# mat = np.array([[1, 2, 3],
#                 [2, 3, 6]])
# new_row1 = np.array([[2, 5 ,7]])

# new_row2 = np.array([[2, 100 ,700]])

# new_mat1 = np.append(mat, new_row1, axis = 0) # already appended

# new_mat2 = np.append(new_mat1, new_row2, axis = 0) # added another row

# print(mat)
# print()
# print(new_mat1)
# print()
# print(new_mat2)

mat = np.array([[1, 2, 3],
                [2, 3, 6]])
new_col = np.array([[1], [2]]) # add 1,2
new_mat = np.append(mat, new_col, axis = 1)
print(mat)
print(new_mat)
