i = 10
if i > 10:
    print('graterthan 10')

print("not in if")

if i > 10:
    print("I am if block")
else:
    print("I am else blovk")

print("I am alone ")

if i == 10:
    print("i is equal to 10")
    if i < 15:
        print("i is also less then 15 nexted if")
    else:
        print("i is no less than 15 nested elsew")

# elif ladder
if i == 1:
    print(" i is 1")
elif i == 2:
    print("i is 2")
elif i == 3:
    print("i is 3")
else:
    print(" i is 10")

# shorthand if  statement
i = 10
if i < 15: print("i is less than 15")

#   shorthand if else
print(True) if i < 15 else print(False)
# chaninig comparision in python 1<x<10 = 1<x and x<10
x = 5
print(1 < x < 10)
print(10 < x < 20)
print(x < 10 < x * 10 < 100)
print(10 > x <= 9)
print(5 == x > 4)

list1 = ["hin", "mur", "avs"]
for i in list1:
    print(i)

list1 = "string"
for i in list1:
    print(i)

d = dict()
d['xyz'] = 123
d['abc'] = 345
for i in d:
    # print("% s % d" %(i, d[i]))
    print(i, d[i])

# continue statement
for i in "geeksforgeeks":
    if i == 'g' or i == 's':
        continue
    print("current letter", i)

# break statement
for i in "geeksforgeeks":
    if i == 'e' or i == 's':
        break
    print("current lettersssss", i)

# pass statemenr to write empty loop
for i in "geeksforgeeks":
    pass
print(i)
# range() in for loop start to end-1
for i in range(10):
    print(i, end=" ")
print()

# while loop
c = 0
while c < 3:
    c = c + 1
    print("hello")

a = [1, 2, 3, 4]
while a:
    print(a.pop())

# single statement while block
c = 0
while c < 5: c += 1; print("hello")

i = 0
a = 'geeksforgeeks'
while i < len(a):
    if a[i] == 'e' or a[i] == 's':
        i += 1
        continue
    print(a[i])
    i += 1

while i < len(a):
    if a[i] == 'e' or a[i] == 's':
        i += 1
        break
    print('Current Letter :', a[i])
    i += 1

row = 1
col = 0
while row <= 5:
    if col < row:
        print("* ", end="")
        col += 1
        continue
    if col == row:
        print(" ", end="")
        row += 1
        col = 0
    print("\n")

# zip() method use to comibine the two object of same type
questions = ['name', 'colour', 'shape']
answers = ['apple', 'red', 'a circle']
for question, answer in zip(questions, answers):
    print('What is your {0}?  I am {1}.'.format(question, answer))

# python code to demonstrate working of iteritems(),items()

d = {"geeks": "for", "only": "geeks"}

# using iteritems to print the dictionary key-value pair
# print("The key value pair using iteritems is : ")
# for i, j in d.iteritems():
#     print(i, j)

# using items to print the dictionary key-value pair
print("The key value pair using items is : ")
for i, j in d.items():
    print(i, j)

# sorted() use to sort the list
lis = [1, 3, 5, 6, 2, 1, 3]
print("The list in sorted order is : ")
for i in sorted(lis):
    print(i, end=" ")

print ("The list in sorted order (without duplicates) is : ")
for i in sorted(set(lis)):
    print(i, end=" ") 


