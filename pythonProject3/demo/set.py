# set has no duplicate elements, mutabable
set1 = set()
print(set1)
set1 = set("geeksforgeeks")
print(set1)
string = 'geeksforgeeks'
set1 = set(string)
print(set1)
set1 = set(["geeks", "for", "geeks"])
print(set1)
set1 = set(['1', '2', '3', '4'])
print(set1)
set1 = set([1, 2, 'geeks', 'for', 3, 3])

# add() method is use for for addign element to the set
set1 = set()
set1.add(8)
set1.add(7)
set1.add(9)
set1.add((5, 8))
for i in range(1, 6):
    set1.add(i)

print(set1)

# to add morethan one elemnet update() method is useful

set1 = set([ 4, 5, (6, 7)])
set1.update([10, 11])
print("\nSet after Addition of elements using Update: ")
print(set1)

# for accessing the element in set
for i in set1:
    print(i, end=" ")

# check for element is present or not in set
print("Geeks" in set1)
# remove() and discard() method use for removing element of set
set1 = set([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
set1.remove(5)
set1.remove(6)
print(set1)
set1.discard(2)
set1.discard(3)
print(set1)

# clear() is used for removing all the elements from the set
set1.clear()
print(set1)


# pop() methos is use for removing element its remove last element and return the last element
set1 = set([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
print("Intial Set: ")
print(set1)

# Removing element from the
# Set using the pop() method
set1.pop()
print("\nSet after popping an element: ")
print(set1)



