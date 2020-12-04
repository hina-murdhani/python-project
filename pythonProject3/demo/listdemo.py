import functools
import operator
from filecmp import cmp

List = []
# blank list
print(List)

# list with number
List = [1, 2, 3, 4]
print(List)

# list with string
List = ["Geeks", "For", "Geeks"]
print(List[0])
print(List[2])

List = [['Geeks', 'For'], ['my', 'Geeks']]
print(List)

# List with duplicatre values and mixed values
List = [2, 4, 5, 2, 4, 4, 5]
print(List)

List = ["Strinf", 3, 5, 7, 'hina']
print(List)

# length of list
List = []
print(len(List))

List = [2, 4, 6]
print(len(List))

# use the append method to add element in list , it will use to add the data at the end
List = []
print(List)
List.append(1)
List.append(2)
List.append(4)
print(List)

for i in range(1, 4):
    List.append(i)

print(List)

# adding tuple to lst
List.append((4, 2))
print(List)

List1 = ["Geeks", "for"]
List.append(List1)
print(List)

# if want to add data in list at particular position use insert() method
List = [1, 2, 3, 4]
List.insert(3, 12)
List.insert(0, "Geeks")
print(List)

# extend() method is use to add the more than one element at the end of list
List = [1, 2, 3, 4]
List.extend("geeks")
print(List)

# can access element using idexing
List = ["Geeks", "For", "Geeks"]

# accessing a element from the
# list using index number
print("Accessing a element from the list")
print(List[0])
print(List[2])
List = [['Geeks', 'For'], ['Geeks']]
print(List[0][1])
print(List[1][0])
List = [1, 2, 'Geeks', 4, 'For', 6, 'Geeks']

# accessing a element using
# negative indexing
print("Accessing element using negative indexing")

# print the last element of list
print(List[-1])

# print the third last element of list
print(List[-3])

# to remove element from list remove() is used it will take element as arg
List = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
List.remove(5)
List.remove(6)
print(List)

for i in range(1, 5):
    List.remove(i)
print("\nList after Removing a range of elements: ")
print(List)

# pop() methos is also use for removing element from list default it will remove last element and return the elemnt
# pop() is taking index as argument

List = [1, 2, 3, 4, 5]
print(List)
List.pop()
print(List)
List.pop(2)
print(List)

List = ['G', 'E', 'E', 'K', 'S', 'F', 'O', 'R', 'G', 'E', 'E', 'K', 'S']
print(List)

# it will print from index 3 till 7
Sliced_List = List[3:8]
print("\nSlicing elements in a range 3-8: ")
print(Sliced_List)

# Print elements from a pre-defined point to end
Sliced_List = List[5:]
print("\nElements sliced from 5th "
      "element till the end: ")
print(Sliced_List)

# Printing elements from beginning till end
Sliced_List = List[:]
print("\nPrinting all elements using slice operation: ")
print(Sliced_List)

List = ['G', 'E', 'E', 'K', 'S', 'F', 'O', 'R', 'G', 'E', 'E', 'K', 'S']
print("Initial List: ")
print(List)

Sliced_List = List[:-6]
print("it will print from beginning to till last 6th elemnt")
print(Sliced_List)

# Print elements of a range using negative index List slicing
Sliced_List = List[-6:-1]
print("\nElements sliced from index -6 to -1")
print(Sliced_List)

# Printing elements in reverse using Slice operation
Sliced_List = List[::-1]
print("\nPrinting List in reverse: ")
print(Sliced_List)

# Append()	Add an element to the end of the list
# Extend()	Add all elements of a list to the another list
# Insert()	Insert an item at the defined index
# Remove()	Removes an item from the list
# Pop()	Removes and returns an element at the given index
# Clear()	Removes all items from the list
# Index()	Returns the index of the first matched item
# Count()	Returns the count of number of items passed as an argument
# Sort()	Sort items in a list in ascending order
# Reverse()	Reverse the order of items in the list
# copy()	Returns a copy of the list

# Python3 program to count the number of times
# an object appears in a list using count() method

lst = ['Cat', 'Bat', 'Sat', 'Cat', 'Mat', 'Cat', 'Sat']
print([[l, lst.count(l)] for l in set(lst)])

print(dict((l, lst.count(l)) for l in set(lst)))

numbers = [1, 3, 4, 2]

# Sorting list of Integers
numbers.sort(reverse=True)

print(numbers)
decimalnumber = [2.01, 2.00, 3.67, 3.28, 1.68]

# Sorting list of Floating point numbers
decimalnumber.sort(reverse=True)


def sortSecond(val):
    return val[1]


lis = [1, 3, 5, 6, 2]
print("sum of all elements", end=" ")
print(functools.reduce(lambda a, b: a + b, lis))

print("maax number")
print(functools.reduce(lambda a, b: a if a > b else b, lis))

# list1 to demonstrate the use of sorting
# using using second key
list1 = [(1, 2), (3, 3), (1, 1)]

# sorts the array in ascending according to
# second element
list1.sort(key=sortSecond)
print(list1)

# sorts the array in descending according to
# second element
list1.sort(key=sortSecond, reverse=True)
print(list1)

lis = [1, 3, 5, 6, 2, ]

# using reduce to compute sum of list
# using operator functions
print(functools.reduce(operator.add, lis))
print(functools.reduce(operator.mul, lis))

# sum() functiom
numbers = [1, 2, 3, 4, 5, 1, 4, 5]

# start parameter is not provided sum(list , start) => list+start only numer is allowes
Sum = sum(numbers)
print(Sum)

# start = 10
Sum = sum(numbers, 10)
print(Sum)

# print average of number
numbers = [1, 2, 3, 4, 5, 1, 4, 5]

# start = 10
Sum = sum(numbers)
average = Sum / len(numbers)
print(average)

# ord() use to get the ASCII value unicode value
value = ord("A")

# writing in ' ' gives the same result
value1 = ord('A')
print(value, value1)

# cmp() to compare two list , 1 if list1>lis2 , -1 if list1<list2 , 0 if both are equal
list1 = [1, 2, 4, 3]
list2 = [1, 2, 5, 8]
list3 = [1, 2, 5, 8, 10]
list4 = [1, 2, 4, 3]
# print(cmp(list2, list1))
# print(cmp(list2, list3))
# print(cmp(list4, list1))

# string is consider grater than integer
list1 = [1, 2, 4, 10]
list2 = [1, 2, 4, 'a']
list3 = ['a', 'b', 'c']
list4 = ['a', 'c', 'b']


# Comparing lists  prints 1 because string at end compared to number string is greater
# print("Comparison of list2 with list1 : ", print(cmp(list2, list1)))

# prints -1, because list3 has an alphabet at beginning even though size of list2 is greater, Comparison
# is terminated at 1st element itself.
# print("Comparison of list2 with list3(larger size) : ", print(cmp(list2, list3)))

# prints -1 as list4 is greater than List3
# print("Comparison of list3 with list4 : ", print(cmp(list3, list4)))


# filter(fun , seq)
def fun(variable):
    letters = ['a', 'e', 'i', 'o', 'u']
    if variable in letters:
        return True
    else:
        return False


sequence = ['g', 'e', 'e', 'j', 'k', 's', 'p', 'r']
filtered = filter(fun, sequence)

for s in filtered:
    print(s)

seq = [0, 1, 2, 3, 5, 8, 13]
result = filter(lambda x: x % 2 != 0, seq)
print(list(result))

result = filter(lambda x: x % 2 == 0, seq)
print(list(result))


# map() returns the map iterable object
def numdob(n):
    return n + n


numb = (1, 2, 3, 4)
result = map(numdob, numb)
print(list(result))

numbers = (1, 2, 3, 4)
result = map(lambda x: x + x, numbers)
print(list(result))

numbers1 = [1, 2, 3]
numbers2 = [4, 5, 6]

result = map(lambda x, y: x + y, numbers1, numbers2)
print(list(result)) 
