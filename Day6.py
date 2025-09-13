  #Looping or iterative statements

  # for loop
fruits = ["apple","Banana","Kiwi","Mango","Watermelon"]
for fruit in fruits:
      print(fruit)

my_list = list(range(1, 11))
print(my_list)

#  i need to print the numbers from 1 to 10
for i in range(1,21,2):
     print(i,end=" ")
my_dic={
     "1": "Apple",
     "2":"Banana",
     "3":"mango"}
for k in my_dic:
   print(f"{k}: {my_dic[k]}")

fruits = ["Apple","Mango","Banana"]
count = 0
for fruit in fruits:
     count = count+1
     print(f"{count} : {fruit}")

#infinite loop

count=0
while count<=10:
     print("My name is Manish ")
     count+=1


for i in range(1,21,2):
    print(i, end = " ")

print()

for j in range(0,21,2):
    print(j, end = " ")
    