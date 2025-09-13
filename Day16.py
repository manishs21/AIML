import numpy as np
# v1 = np.array([1,2])
# v2 = np.array([2,3])

# v_sum = v1 + v2
# print(v_sum)

# v = np.array([1,2,3,4,5,8,90,100])
# n_v = np.linalg.norm(v)
# print(n_v)

# v1 = np.array([55,-1,3,42])
# v2 = np.array([2,2,2,22])

# # is_ortho = (np.dot(v1, v2) ==0)
# # print(is_ortho)

# proj = (np.dot(v1,v2) / np.dot(v2, v2)) * v2  # output will scalar so multiply sign is used
# print(proj)

# M = np.array([[1,2], [3,4], [5,6]])
# c1, c2 = 1.5, 2
# l_c = c1 * M[0] + c2 * M[1]  #linear combination
# print(l_c)

# M = np.array([[1,2,3], [3,4,5], [5,6,7]])
# c1, c2 = 1.5, 2
# l_c = c1 * M[0] + c2 * M[1]  #linear combination
# print(l_c)

v1 = np.array([1,2,3])
v2 = np.array([2,2,2])

M = np.stack([v1, v2], axis = 1)

r = np.linalg.matrix_rank(M)
is_independent = (r == M.shape[1])

if is_independent:
    print("The vectors are independent")
    
else:
    print("The vectors are dependent")
    
    print("The vectors are independent")

