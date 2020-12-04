# dictionary contains key value pair and keys are immutable nd its unordered , keys are case sensitive
dict1 = {1: 'geeks', 2: 'for', 3: 'geeks'}
print(dict1)
dict1 = {1: 'geeks', 2: [2, 3], 'name': 'for'}
print(dict1)
dict1 = dict({1: 'geeks', 2: 'for', 3: 'geeks'})
print(dict1)
dict1 = dict([(1, 'geeks'), (2, 'for')])
print(dict1)
# nested dictionary
dict1 = {1: 'geesk', 2: 'for', 3: {'a': '1', 'b': '2'}}
print(dict1)
# we can add value in dict using dict[key]=value
dict1 = {}
dict1[0] = 'geeks'
dict1[2] = 'for'
dict1[4] = 'geeks'
print(dict1)
dict1['value'] = 2, 3, 4
print(dict1)
# we can access element from dictionary using key

Dict = {1: 'Geeks', 'name': 'For', 3: 'Geeks'}

# accessing a element using key
print("Accessing a element using key:")
print(Dict['name'])

# using the get() method we can access the element of dict
Dict = {1: 'Geeks', 'name': 'For', 3: 'Geeks'}
print(Dict.get(3))

Dict = {'Dict1': {1: 'Geeks'}, 'Dict2': {'name': 'hina'}}
print(Dict['Dict1'])
print(Dict['Dict2']['name'])
# del is use for deleting the dictionary
Dict = {5: 'Welcome', 6: 'To', 7: 'Geeks',
        'A': {1: 'Geeks', 2: 'For', 3: 'Geeks'},
        'B': {1: 'Geeks', 2: 'Life'}}
del Dict[6]
print(Dict)
del Dict['A'][2]
print(Dict)

# pop() is use for deleting the element in dictionary of perticulr key
Dict = {1: 'Geeks', 'name': 'For', 3: 'Geeks'}

# Deleting a key
# using pop() method
pop_ele = Dict.pop(1)

# popitem() is use for deleting the random key value pair and return the key value pair
Dict = {1: 'Geeks', 'name': 'For', 3: 'Geeks'}

# Deleting an arbitrary key
# using popitem() function
pop_ele = Dict.popitem()
print("\nDictionary after deletion: " + str(Dict))
print("The arbitrary pair returned is: " + str(pop_ele))

# all item of dictionary can be deleted  using clear() method
Dict.clear()
print(Dict)
