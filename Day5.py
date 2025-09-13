# num = -5
# if a > 0:
#     print("The number is positive")

# else:
#     print("The number is negative")

# num = int(input("Enter a number:"))
# if num > 0:
#     print("The number is positive")
# elif num < 0:
#     print("The number is negative")
# else:
#     print("The number is zero")

# num = int(input("Enter a number:"))
# if num % 2 == 0:
#     print("The number is even")
# else:
#     print("The number is odd")

# num1 = int(input("Enter a number:"))
# num2 = int(input("Enter a number:"))
# num3 = int(input("Enter a number:"))

# if num1 > num2:
#     if num1 > num3:
#         print("The number 1 is greater")

# if num2 > num1:
#     if num2 > num3:
#         print("The number 2 is greater")

# else:
#     print("The number 3 is greater")        

        
# num1 = int(input("Enter a number:"))
# num2 = int(input("Enter a number:"))
# num3 = int(input("Enter a number:"))

# if (num1 >= num2) and (num1 >= num3):
#     print(f"The greater number is {num1}")
# elif (num2 >= num1) and (num2 >= num3):
#     print(f"The greater number is {num2}")
# else:
#     print(f"The greater number is {num3}")
    
num1 = int(input("Enter a number:"))
num2 = int(input("Enter another number:"))

ch = int(input("Enter:\n1. for Addition\n2. for Substraction\n3. for Product"))

match ch:
    case 1:
        add = num1 + num2
        print(f"{num1} + {num2} = {add}")
    case 2:
        if num1 > num2:
            sub = num1 - num2
            print(f"{num1} - {num2} = {sub}")
        else:
            sub = num2 - num1
            print(f"{num2} - {num1} = {sub}")
    case 3:
            pro = num1 * num2
            print(f"{num1} * {num2} = {pro}")