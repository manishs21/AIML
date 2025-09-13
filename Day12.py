import numpy as np

# arr_3d = np.array([[[2, 3, 5], [6, 8, 9]], [[3, 5, 6], [4, 5, 6]]])
# print(arr_3d)

# # 3 x 3 matrix with all element zero
# zeros_a = np.zeros((3, 3))
# print(zeros_a)

# # 4 x 4 matrix with all element one
# ones_a = np.ones((3, 3))
# print(ones_a)

# # to create an identity matrix of size 5 x5 
# id_mat = np.eye(5)
# print(id_mat)

# # we have to crate array of first 50 numbers starting from 1
# arr = np.arange(1, 51)
# print(arr)

# #even numbers from 2 to 100
# arr = np.arange(2, 101, 2)
# print(arr)

# #we need an array having five values from 1 to 10 evenly spaced/ equal gap
# sp_arr = np.linspace(1, 10, 5)
# print(sp_arr)

# #this create a random 4 x 4 matrix between 0 to 1
# random_arr = np.random.rand(4, 4)
# print(random_arr)

# # to generate randon values from 1 to 10
# random_arr = np.random.randint(1, 11, size = (3, 3))
# print(random_arr)

# arr = np.array([[10, 20, 30], [30, 40, 70], [3, 5 ,7]], dtype= "int16")
# print(arr)
# print(arr.shape) # 3 by 3 matrix
# print(arr.size) # total number of element
# print(arr.ndim) # dimension of array 2D
# print(arr.dtype) # data type int or float or string
# print(arr.itemsize) # size of each element in size
# print(arr.nbytes) # Total memory usages

# arr_id = np.array([10, 20, 30, 40, 50])
# print(arr_id[1:4]) #step slicing

# arr_id = np.array([10, 20, 30, 40, 50])
# print(arr_id[::2]) # equal 2 step gap #not enclusive

arr_2d = np.array([[10, 20, 30], [40, 50, 60], [70, 80, 90]])
print(arr_2d)
print(arr_2d[2, :])
print(arr_2d[:, 1])
print(arr_2d[::2, 2])
print(arr_2d[::2, 0])
print(arr_2d[1,1:])
print(arr_2d[0, 0:])



