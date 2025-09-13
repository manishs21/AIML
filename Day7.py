# def greet(n):
#     print(f"Welcome {n}")


# name = input("Enter your name:")
# greet(name)



# def greet(name = "Manish"):
#     print(f"Welcome {name}")

# def main():
#     name = input("Enter your name:")
#     greet()
#     greet(name)
# main()    


def celsius_to_farenheite(celsius):
    farenheite = (celsius * 9/ 5) + 32
    return farenheite

def main():
    celsius = float(input("Enter temperature in Celsius:"))
    feren = celsius_to_farenheite(celsius)
    print (f"Temperature in farenheit = {feren:.2f} degree farenheit")

main()
