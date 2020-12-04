def evenOdd(x):
    if x % 2 == 0:
        print("evern")
    else:
        print("odd")


evenOdd(10)
evenOdd(5)


# default arg
def myfun(x, y=50):
    print(x)
    print(y)


myfun(10)


# keyword argument
def std(fname, lname):
    print(fname, lname)


std(fname='hina', lname='mur')


# variable length arg
def mydef(*argv):
    for arg in argv:
        print(arg)


mydef('hello', 'hina', 'murdhani')


def dectfun(**args):
    for key, value in args.items():
        print(key, value)


dectfun(name='hina', sur='mur', sis='far')

# annonymous function -> function without name lambda keyword use for creating this function
cube = lambda x: x * x * x

print(cube(7))


# Yield can produce a sequence of values. We should use yield when we want to iterate over a sequence,
# generator are the simple functions but its use the yield

def nextSquare():
    i = 1
    while True:
        yield i * i
        i += 1


for num in nextSquare():
    if num > 100:
        break
    print(num)


def simpleGeneratorFun():
    yield 1
    yield 2
    yield 3


# x is a generator object
x = simpleGeneratorFun()

# Iterating over the generator object using next
print(x.__next__())  # In Python 3, __next__()
print(x.__next__())
print(x.__next__())


# generator using yield
def fib(limit):
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a + b


x = fib(5)
for i in fib(5):
    print(i)


def fi(limit):
    n1 = 0
    n2 = 1
    yield n1
    yield n2
    for j in range(2, limit):
        n3 = n1 + n2
        yield n3
        n1 = n2
        n2 = n3


fi(5)

for i in fi(5):
    print(i)
