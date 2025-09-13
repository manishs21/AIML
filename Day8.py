# Error
# print("Hello World ) -> Syntax error

# num1 = int(input("Enter a number:"))
# num2 = int(input("Enter another number:"))

# sum = num1 - num2 # This represents logical error
# print(f"sum = {sum}")

#Exceptions
# x = int(input("Enter a no:"))
# print(x)

# try:
#     x = int(input("Enter a no:"))
#     print(f"no = {x}")

# except ValueError:
#     print("Please Enter an Integer!! ")
# else:
#     print(f"number = {x}")

# while True:
#     try:
#         x = int(input("Enter a number"))
#     except ValueError:
#         print("Please enter an Integer!!")
#     else:
#         break
# print(f"The entered number is: {x}")

# while True:
#     try:
#         x = int(input("Enter a number:"))
#     except ValueError:
#         pass
#     else:
#         break
# print(f"The entered number is: {x}")

# while True:
#     try:
#         x = int(input("Enter a number: "))
#         result = 10/x
        
#     except ValueError:
#         print("Please enter an integer")

#     except ZeroDivisionError:
#         print("The Divisor cannot be zero")

#     else: 
#         break
    
# print(f"Result = {result}")


# while True:
#     try:
#         x = int(input("Enter a number: "))
#         result = 10/x
        
#     except ValueError:
#         pass

#     except ZeroDivisionError:
#         pass

#     else: 
#         break
    
# print(f"Result = {result}")

# def main():
#     try:
#         a = int(input("Enter a num: "))
#         b = int(input("Enter a num: "))
#         c = int(input("Enter a num: "))
#     except ValueError as e:
#         print("Invalid input! Please enter integers only.")
#         return

#     s = sum(a, b, c)
#     print(f"Sum: {s}")

#     p = product(a, b, c)
#     print(f"Product: {p}")

#     o = operation(a, b, c)
#     print(f"Operation (a + b) / c: {o}")
# def operation(a, b, c):
#     try:
#         d = (a + b) / c
#     except ZeroDivisionError as e:
#         print("ZeroDivisionError:", e)
#     else:
#         return d

# def sum(a, b, c):
#     return a + b + c

# def product(a, b, c):
#     return a * b * c

# main()


while True:
    try:
        num1 = int(input("Enter a number: "))
        num2 = int(input("Enter another number: "))
        num3 = int(input("Enter another number: "))
        
        operation = (num1+num2)/num3
        
    except ValueError:
        pass

    except ZeroDivisionError:
        pass

    else:
        sum = num1 + num2 + num3
        product = num1 * num2 * num3
        print(f"sum = {sum}")
        print(f"Product = {product}")
        print(f"Operation = {operation}")