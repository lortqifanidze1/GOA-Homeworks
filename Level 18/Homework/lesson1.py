a = int(input("please enter yur first num"))
b = int(input("plase enter your second num"))

list = []

for i in range (a,b):
    list.append(i)
print(sum(list))
print(min(list))
print(max(list))