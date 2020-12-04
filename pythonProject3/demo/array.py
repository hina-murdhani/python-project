import array as arr

# by importing array module we can generate the array
a = arr.array('i', [1, 2, 3])
for i in range(0, 3):
    print(a[i])

a = arr.array('d', [1.3, 4.5, 6.7])
for i in range(0, 3):
    print(a[i])

# can add element in array using insert():- at any index ,method and append() method : at the end of array
a = arr.array('i', [1, 3, 4])
a.insert(1, 4)
for i in range(0, len(a)):
    print(a[i])
a.append(5)
for i in range(0, len(a)):
    print(a[i])

# can access element using the index for array
a = arr.array('i', [1, 2, 3, 4, 5, 6])

# accessing element of array
print("Access element is: ", a[0])

# accessing element of array
print("Access element is: ", a[3])

# remove() use to remove particular element , pop() return thee removed element , can remove element at particular index
a = arr.array('i', [1, 2, 3, 1, 5])
a.pop(2)
for i in range(0, len(a)):
    print(a[i])

a.remove(1)
for i in range(0, len(a)):
    print(a[i])

# array slicing
l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

a = arr.array('i', l1)
slice_arr = a[3:8]
print(slice_arr)
slice_arr = a[5:]
print(slice_arr)
slice_arr = a[:]
print(slice_arr)

# searching the element in array using index() method
a = arr.array('i', [1, 2, 3, 1, 2, 5])
print(a.index(2))
print(a.index(1))

# for updating the element in array we need to just reassign the value to that index
a = arr.array('i', [1, 2, 3, 1, 2, 5])

# printing original array
print("Array before updation : ", end="")
for i in range(0, 6):
    print(a[i], end=" ")

print("\r")

# updating a element in a array
a[2] = 6
print("Array after updation : ", end="")

for i in range(0, 6):
    print(a[i], end=" ")
print()


for i in reversed(range(1, 10, 3)):
    print(i)

