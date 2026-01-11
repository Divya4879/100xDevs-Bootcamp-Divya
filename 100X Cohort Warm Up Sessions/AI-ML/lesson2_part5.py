# Lambda Functions - Anonymous functions with expressions

lambda num: num ** 2

mult = lambda a, b, c : a*b*c
print(mult(2,7,8))

# Map, Filter and Reduce Functions

# map()

nums= [2,9,7]

def square(num):
    return num ** 2

print(list(map(square,nums)))  # [4, 81, 49]


sq = lambda num:num ** 2

print(list(map(sq,nums))) # Same result, with lambda functions

# This works the same 

print(list(map(lambda num:num ** 2,nums)))  # no other variable even needed

# filter()
# Filters sequences based on a function, something like that

nums = [1,2,3,4,5,6]

print(list(filter(lambda num:num%2 == 0,nums))) # [2, 4, 6]

#reduce()

expenses = [
    ("binding", 150),
    ("cohort", 5400),
    ("printouts", 50)
]

sum = 0

for expense in expenses:
    sum += expense[1]

print(sum)

# OR, using reduce
# reduce(function, iterable, initial_value)


from functools import reduce

expenses = [
    ("binding", 150),
    ("cohort", 5400),
    ("printouts", 50)
]

print(reduce(lambda a, b: a + b[1], expenses, 0))  # 5600

# Recursion - function called itself

def factorial(n):
    while n>0:
        return n * factorial(n-1)
    return 1

print(factorial(4))

# DECORATORS

def logtime(func):
    def wrapper():
        print("Before")
        value = func()
        print("After")
        return value
    return wrapper

@logtime  # logtime function added as decorator to the function below this line
def hello():
    print("Hello dearie!")

hello()

"""
Returns this on terminal:-

Before
Hello dearie!
After

"""

# Docstrings

"""
Docs- starting of a file, inside a function, for others and yourself-docs
"""

def example():
    """
    Docstring for list friend- different methods
    """
    friend = []
    friend.append("myself")
    friend[1] = "mum"
    friend.pop()

print(help(example)) # uses docstrings

# Annotations- optional, for specifying types

def increment(n):
    n += 1
    return n

print(increment(5.1))

# Using annotations

def increment(n: int) -> int:  # specifies that this function only takes in int as input and returns int as output.
    n += 1
    return n

print(increment(5))

# Exceptions

"""

try:
    # some lines of code
except <ERROR1>:
    # handler <ERROR1>
except <ERROR2>:
    # handler <ERROR2>
except:
    # Handles all other errors
else:
    # no exception was raised, the code ran
finally:
    # always runs at the end

some examples of error:-

while reading a file, EOFError - end of file error
num/0 - ZeroDivisionError

"""

try:
    res = 2 / 0
except ZeroDivisionError:
    print("Can't divide any no by 0, silly!")
finally:
    res = 1

print(res) # 1


# Raising an exception

# raise Exception("An error!")

try:
    raise Exception("An error!")
except Exception as error:
    print(error)   # An error!


class DogNotFoundException(Exception):
    print("inside")
    pass # just used on an empty class/function

try:
    raise DogNotFoundException()
except DogNotFoundException:
    print("Dog not found!")     

# prints this-

# inside
# Dog not found!

# With keyword

# without using it

filename = '/Users/Flavio/text.txt'

try:
    file = open(filename,"r")
    content = file.read()
    print(content)

finally:
    file.close()

# using with

filename = '/Users/Flavio/text.txt'

with open(filename,"r") as file:
    content = file.read()
    print(content)

# here, using with keyword, it automatically closes the file after its executed.