import operator

from pip._vendor.distlib.compat import raw_input

# to take input from user in console
val = input("Please enter  your name")
print(val)
print(type(val))

val1 = raw_input("enter your name")
print(val1)

input1 = input()
print(input1)
# typecast to int
# input2 = input()
# print(int(input2))

# taking multiple input from user use split() method
x, y = input("enter two values").split()
print(x)
print(y)

a, b, c = input("enter 3 value").split()
print(a, b, c)

t = list(map(int, input("Enter a multiple value: ").split()))
print("List of students: ", t)

# using comprehensive list we can take multiple input from user
m, n = [int(x) for x in input("please enter 2 values").split()]
print(m, n)

t = [int(x) for x in input("enter multiple values").split()]
print(t)

# to print in single line
print("geeks", end=" ")
print("geeksforgeeks")

# for seperating the text by any symbol
# for formatting a date
print("09", "12", "2016", sep='-')

print('prtk', 'agarwal', sep='', end='@')
print('geeksforgeeks')

# remaining with python format
# Pyhton Operators Arithmatic operator

val3 = input("enter first values")
val4 = input("enter second value")
val1 = int(val3)
val2 = int(val4)
add = val1 + val2
add = val1 + val2
sub = val1 - val2
# return float
div = val1 / val2
# return floar
div1 = val1 // val2
mul = val1 * val2
mod = val1 % val2
p = val1 ** val2
print(add, sub, div, mul, p, mod, div1)

# Relational Operator
print(val1, val2)
print(val1 > val2)
print(val1 < val2)
print(val1 == val2)
print(val1 != val2)
print(val1 >= val2)
print(val1 <= val2)

# Logical operator and , or , not
a = True
b = False
print(a and b)
print(a or b)
print(not a)

# Bitwise Operator &And  | Or ~Not  ^Xor  >>right shift  <<left shift
# 0101
q = 10
# 0010
p = 4
print(q | p)
print(q & p)
print(q ^ p)
print(~q)
print(q >> 2)
print(q << 2)

# Assignment Operator =,+=,-=,*=,/=,%=,//=,**=,&=,
# Special Operator is , is not
a1 = 3
b1 = 3
print(a1 is not b1)
print(a1 is b1)

# membership operator in, not in
x = 'Geeks for Geeks'
print('G' in x)
print('Geeks' not in x)

# ternary operator [on_true] if [expression] else [on_false]
a, b = 10, 20

# Copy value of a in min if a < b else copy b
mini = a if a < b else b

# ternary ope with if else
print(mini)
print("a and b are equal" if a == b else "a is graterthan b" if a > b else "a is lessthan b")
# with if else
if a != b:
    if a > b:
        print("a is grater than b")
    else:
        print("a is lessthan b")
else:
    print("a is equal to b")

# operator overloading
print(1 + 2)

# concatenate two strings
print("Geeks" + "For")

# Product two numbers
print(3 * 4)

# Repeat the String
print("Geeks" * 4)


class A:
    def __init__(self, s):
        self.s = s

    def __add__(self, other):
        return self.s + other.s


ob1 = A(1)
ob2 = A(2)
ob3 = A("Geeks")
ob4 = A("For")
print(ob1 + ob2)
print(ob3 + ob4)


class Complex:
    def __init__(self, s1, s2):
        self.s1 = s1
        self.s2 = s2

    def __add__(self, other):
        return self.s1 + other.s1, self.s2 + other.s2

    def __str__(self):
        return self.s1, self.s2


obj1 = complex(2, 3)
obj2 = complex(3, 4)
obj3 = obj1 + obj2
print(obj3)

# Any Returns true if any of the items is True
# return false
print(any([False, False, False, False]))
# return true
print(any([False, True, False, False]))
# return true
print(any([True, False, False, False]))

# All Returns true if all of the items are True (or if the iterable is empty).
# return true
print(all([True, True, True, True]))
# return false
print(all([True, True, True, True]))
# return false
print(all([False, False, False]))

# method for operator need to import operator
# add(a, b),sub(a, b),mul(a, b),truediv(a, b),floordiv(a, b),pow(a, b),mod(a, b),lt(a, b),le(a, b),eq(a,b),
# gt(a,b),ge(a,b),ne(a,b)
print(operator.add(3, 4))
print(operator.sub(3, 4))

if operator.lt(3, 4):
    print("3 is less than 4")
else:
    print("3 is not less than 4")

# setitem(ob, pos, val) ,ob[pos] = val
# delitem(ob, pos) , del ob[pos]
# getitem(ob, pos) , ob[pos]

li = [1, 5, 6, 7, 8]
for i in range(0, len(li)):
    print(li[i], end=" ")

# [1, 5, 6, 3, 8]
operator.setitem(li, 3, 3)
print("The modified list after setitem() is : ", end="")
for i in range(0, len(li)):
    print(li[i], end=" ")

# [1, 6, 3, 8]
operator.delitem(li, 1)
print("The modified list after delitem() is : ", end="")
for i in range(0, len(li)):
    print(li[i], end=" ")
# 8
print("The 4th element of list is : ", end="")
print(operator.getitem(li, 3))

# setitem(ob, slice(a,b), vals) ,obj[a:b] = vals
# delitem(ob, slice(a,b)) , del obj[a:b]
# getitem(ob, slice(a,b)) , obj[a:b]


li = [1, 5, 6, 7, 8]

# printing original list The original list is : 1 5 6 7 8
print("The original list is : ", end="")
for i in range(0, len(li)):
    print(li[i], end=" ")

print("\r")

# using setitem() to assign 2,3,4 at 2nd,3rd and 4th index
# The modified list after setitem() is : 1 2 3 4 8
operator.setitem(li, slice(1, 4), [2, 3, 4])

# printing modified list after setitem()
print("The modified list after setitem() is : ", end="")
for i in range(0, len(li)):
    print(li[i], end=" ")

print("\r")

# using delitem() to delete value at 3rd and 4th index
# The modified list after delitem() is : 1 2 8
operator.delitem(li, slice(2, 4))

# printing modified list after delitem()
print("The modified list after delitem() is : ", end="")
for i in range(0, len(li)):
    print(li[i], end=" ")

print("\r")

# using getitem() to access 1st and 2nd element
# The 1st and 2nd element of list is : [1, 2]
print("The 1st and 2nd element of list is : ", end="")
print(operator.getitem(li, slice(0, 2)))

# concat(ob1,obj2) :  obj1 + obj2
# contains(ob1,obj2): obj2 in obj1
s1 = "geeksfor"

# Initializing string 2
s2 = "geeks"

# using concat() to concatenate two strings
print("The concatenated string is : ", end="")
print(operator.concat(s1, s2))

# using contains() to check if s1 contains s2
if operator.contains(s1, s2):
    print("geeksfor contains geeks")
else:
    print("geeksfor does not contain geeks")

# The == operator compares the values of both the operands and checks for value equality.
# Whereas is operator checks whether both the operands refer to the same object or not.

# in oprator
list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9]
for item in list1:
    if item in list2:
        print("overlapping")
else:
    print("not overlapping")

# not in operator:Evaluates to true if it does not finds a variable in the specified sequence and false otherwise
x = 24
y = 20
li = [10, 20, 30, 40, 50]

if x not in li:
    print("x is NOT present in given list")
else:
    print("x is  present in given list")

# is opertaor : Evaluates to true if the variables on either side of the operator point to the same object and false
# otherwise.
x = 5
if type(x) is int:
    print("true")
else:
    print("false")

# ‘is not’ operator – Evaluates to false if the variables on either side of the operator point to the same object and
# true otherwise.
x = 5.2
if type(x) is not int:
    print("true")
else:
    print("false")

# datatypes
# String
a = "This is string"
print(a)

# Lists A single list can contain strings, integers, as well as objects. Lists can also be used for implementing
# stacks and queues. Lists are mutable, i.e., they can be altered once declared.


L = [1, "a", "string", 1 + 2]
print(L)
L.append(6)
print(L)
L.pop()
print(L)
print(L[1])

# tuples : Tuples are just like lists with the exception that tuples cannot be changed once declared.
# Tuples are usually faster than lists.
tup = (1, "a", "string", 1 + 2)
print(tup)
print(tup[1])

i = 1
while i < 10:
    i += 1
    print(i)

for i in range(0, 10):
    print(i)
    
