String1 = "GeeksForGeeks"
print("Initial String: ")
print(String1)

# Printing First character
print("\nFirst character of String is: ")
print(String1[0])

# Printing Last character
print("\nLast character of String is: ")
print(String1[-1])
String1 = "GeeksForGeeks"
print("Initial String: ")
print(String1)
# slicing
# Printing 3rd to 12th character print till 11th
print("\nSlicing characters from 3-12: ")
print(String1[3:12])

# Printing characters between
# 3rd and 2nd last character
print("\nSlicing characters between " +
      "3rd and 2nd last character: ")
print(String1[3:-2])
# updating original string
String1 = "Hello, I'm a Geek"
print("Initial String: ")
print(String1)

# Updating a String
String1 = "Welcome to the Geek World"
print("\nUpdated String: ")
print(String1)

# deleting entire string
String1 = "Hello, I'm a Geek"
print("Initial String: ")
print(String1)

# Deleting a String
# with the use of del
del String1
print("\nDeleting entire String: ")
print(String1)
# If want to print single doublel quote in string use the triple quote or use the escpe


# String Formating
String2 = "{} {} {}".format('Geeks', 'For', 'Life')
print(String2)

String2 = "{1} {0} {2}".format('Geeks', 'For', 'Life')
print(String2)

String2 = "{l} {f} {g}".format(g='Geeks', f='For', l='Life')
print(String2)

# Formatting of integers
String2 = "{0:b}".format(16)
print("\nBinary representation of 16 is ")
print(String2)

String2 = "{0:e}".format(156.6757)
print("\nExponent representation of 156.6757 is ")
print(String2)

String1 = "|{:<10}|{:^10}|{:>10}|".format('Geeks', 'for', 'Geeks')
print("\nLeft, center and right alignment with Formatting: ")
print(String1)

# To demonstrate aligning of spaces
String1 = "\n{0:^16} was founded in {1:<4}!".format("GeeksforGeeks", 2009)
print(String1)

String1 = "{0:.2f}".format(1/6)
print("\none-sixth is : ")
print(String1)
