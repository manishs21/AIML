import numpy as np

# arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
# re_arr = arr.reshape(5, 2)
# print(arr)
# print()
# print(re_arr)

# arr_id = np.array([10, 20, 30, 40])

# for num in arr_id:
#     print(num, end = " ")

# arr_2d = np.array([10, 20, 30],
#                   [40, 50, 60])

# for ls in np.nditer(arr_2d):
#     print(ls)
    
# a = np.array([1, 2, 3, 4])
# b = np.array([5, 6, 7, 8])

# add = a + b
# sub = a - b
# pro = a * b
# div = a / b
# exp = b ** 5
# re = b % a
# print(f"Addition of two arrays element wise = {add}")
# print()
# print(f"Subtraction of two arrays element wise = {sub}")
# print()
# print(f"product of two arrays element wise = {pro}")
# print()
# print(f"Division of two arrays element wise = {div}")
# print()
# print(f"Each element of array {b} raised to the power 5 gives: {exp}")
# print()
# print(f"Reaminder of {b} divides by {a} element wise gives: {re}")
# print()


# arr = np.arange(1, 51)
# sq_rt = np.sqrt(arr)
# s = np.sin(arr)
# c = np.cos(arr)
# t = np.tan(arr)
# n_log = np.log(arr)
# ten_log = np.log10(arr)
# exp = np.exp(arr)

# print(f"sqrt = {sq_rt}")
# print()
# print(f"sin = {s}")
# print()
# print(f"cos = {c}")
# print()
# print(f"tan = {t}")
# print()
# print(f"Natural_log = {n_log}")
# print()
# print(f"log base 10 = {ten_log}")
# print()
# print(f"e ^ x = {exp}")
# print()

# data = np.array([10, 20, 30, 40, 50])

# me = np.mean(data)
# md = np.median(data)
# sd = np.std(data)
# v = np.var(data)
# minn = np.min(data)
# maxx = np.max(data)

# print(me)
# print(md)
# print(sd)
# print(v)
# print(minn)
# print(maxx)
# print(np.argmin(data))
# print(np.argmax(data))

# arr = np.array([1, 2, 3, 4, 1, 3, 2, 4])
# uni_arr, count = np.unique(arr, return_counts = True)
# print(uni_arr)
# print(count)


arr_2d = ([1, 2, 4],
          [4, 6, 9],
          [1, 2, 4],
          [1, 2, 3])
uni = np.unique(arr_2d)
print(uni)


9702187444