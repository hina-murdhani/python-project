# tuples are immutable(cant change)
tuple1 = (5, 'wec', '7', 'my')
print(tuple1)
tuple1 = (1, 3, 4, 5)
tuple2 = ('geeks', 'my', 'weec')
tuple3 = (tuple1, tuple2)
print(tuple3)
Tuple1 = ('Geeks',) * 3
print("\nTuple with repetition: ")
print(Tuple1)
tuple1 = tuple("geeks")
print(tuple1)

# tuple unpacking
tuple1 = ('geeks', 'my', 'for')
a, b, c = tuple1
print(a, b, c)

# tuple concatination
tuple1 = (1, 2, 3, 4)
tuple2 = ('geeks', 'my', 'for')
tuple3 = tuple1 + tuple2
print(tuple3)

Tuple1 = tuple('GEEKSFORGEEKS')

# Removing First element
print("Removal of First Element: ")
print(Tuple1[1:])

# Reversing the Tuple
print("\nTuple after sequence of Element is reversed: ")
print(Tuple1[::-1])

# Printing elements of a Range
print("\nPrinting elements between Range 4-9: ")
print(Tuple1[4:9])
# deleting the tuple
Tuple1 = (0, 1, 2, 3, 4)
del Tuple1

x = [2, 8, 1, 4, 6, 3, 7]
print(sorted(x))
print(sorted(x, reverse=True))
# original list will not modified
print(x)

# sorting of list
x = ['q', 'w', 'e', 'r', 't', 'y']
print(sorted(x))
# sorting of tuple
x = ('q', 'w', 'e', 'r', 't', 'y')
print(sorted(x))
# string sorting
x = "python"
print(sorted(x))
# sorting of dictionary
x = {'q': 1, 'w': 2, 'e': 3, 'r': 4, 't': 5, 'y': 6}
print(sorted(x))
# sorting of set
x = {'q', 'w', 'e', 'r', 't', 'y'}
print(sorted(x))

# custom sorting using key parameter
lis = ["ccc", "bb", "aaaa", "d"]
print(sorted(lis))

# sorting with len fuc

print(sorted(lis, key=len))


def func(p):
    return p % 7


L = [15, 3, 11, 7]
print(sorted(L))
print(sorted(L, key=func))

# tuple() use to convert iterable to tuple
tuple1 = tuple()
print(tuple1)

# when an iterable(e.g., list) is passed
list1 = [1, 2, 3, 4]
tuple2 = tuple(list1)
print(tuple2)

# when an iterable(e.g., dictionary) is passed
dict = {1: 'one', 2: 'two'}
tuple3 = tuple(dict)
print(tuple3)

# when an iterable(e.g., string) is passed
string = "geeksforgeeks"
tuple4 = tuple(string)
print(tuple4) 
