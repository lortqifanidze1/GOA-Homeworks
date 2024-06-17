for i in range(20):
    print(i)



num = int(input("enter num :"))

if num == 2 or  num == 4 or  num == 6 or num == 8 or num ==10 or num == 12 or num == 14 or num ==16 or num == 18 or num ==20:
    print("you win")
else:
    print("you lost")
num1 = 0

while num1 !=20:
    print(num1)
    num1 = num1 + 2
num3 = 0
for i in range(49,100):
    i += 1
    num3 = num3 + i
    print(num3 )
num2 = 1
for i in range (1, 51):
    i +=1 
    num2 = num2 * 5
    print(num2)

num4 = int(input("enter your number "))
num5 = int(input("enter your second number"))
if num5>=num4:
    print("metia")

num6 = int(input("Please enter your first number:"))
num7 = int(input("Please enter your second number:"))
if num6 < num7:
    smallest = num6
    largest = num7
else :
 smallest = num7 
 largest = num6
 for i in range (smallest , largest +1 ):
    print(i, end= " ")


for i in range(5, 11):
    result = i * i
    print(f". {i} . {result}")
