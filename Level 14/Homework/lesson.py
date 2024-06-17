i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1
  
  i = 4
while i < 8:
  print(i)
  continue
  i += 4

  i = 3
while i < 6:
  print(i)
  
  i += 3

  i = 12
while i < 24:
  print(i)
  
  i += 12

i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")

fruits = ("vashli", "banani", "atami")
for x in fruits:
  print(x)

  
for x in "banani":
  print(x)

fruits = ("vashli", "banani", "atami")
for x in fruits:
  print(x)
  if x == "banani":
    break

fruits = ("vashli", "banani", "atami")
for x in fruits:
  if x == "banani":
    continue
  print(x)


for x in range(6):
  print(x)

a = 21
b = 22
if b > a:
  print("22>21")


a = 5
b = 5
if b > a:
  print("b>a")
elif a == b:
  print("b==a")


a = 200
b = 33
if b > a:
  print("b > a")
elif a == b:
  print("a == b ")
else:
  print("a > b")

a= 32 
b = 21 
if a > b:
  print("b>a")
elif a < b:
 print("a>b")
else :
    print("an tolai an arasworea")