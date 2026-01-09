# comment here

""""
docs like this
"""

name = "Divya"
print(type(name) == str)  #True

# silly mistake
print(type(name) == "str")  #False

print(isinstance(name, str))

# Data Types

age = 20
print(isinstance(age, int))

age = 20.5 #Side-eyes
print(isinstance(age, float))

# Class Constructors

age = 20

print(isinstance(str(age), str)) #True

print(isinstance(float(age), float)) #True

print(isinstance(age, int)) #True

# Arithmetic Operators

print(4%3)
print(7//2) # floor division- rounds down to nearest whole no.

print("Divya" + " is so awesome!")

age = 10
age += 10
print(age)

# Boolean Operators

condition1 = True
condition2 = False

print(condition1 and condition2)
print(not condition1)
print(condition1 or condition2)

print(0 or 1) # 1
print([] or False) # False

# Bitwise operators- Rarely used, but well, you "should" know of these

"""
& - Binary and
| - Binary or
^ - Binary XOR
~ - Binary not
<< - Shift Left Operation
>> - Shift Right Operation
"""

# is & in operators- Identity & Membership operators respectively

# Ternary Operator

# def is_awesome():
#     name = input("Enter your name: ")
#     if name == "Divya":
#         print("You're awesome Divya:)))")
#     else:
#         print("You're ok:(")

# is_awesome()

def is_awesome():
    name = input("Enter your name: ")
    return "You're awesome Divya:)))" if name=="Divya" else "You're ok:("

is_awesome()

# Strings

# Multi-Line Strings

intro = """
Hello All!
It's Divya!
You knew me already? Nothing new for you then!
You didn't?
Hello and goodbye then:)
"""

print(intro)

# String Methods

name = "Divya Singh"

print(name.lower())
print(name.upper())
print(name.title())
print(name.isdecimal())
print(name.islower())
print(name.isalpha())
print(name.isalnum())
print(name.startswith("D"))
print(name.capitalize())
print(name.replace("Divya","Ria"))
print(name.split(" "))
print("     Divya".strip())

print("Divya".find("v"))

print(len(name))

print("ivya" in name)

# Escaping Characters

print("\"Divya is sweet\"")

# String Characters and Slicing

name = "Issabella Henry Malfoy"
print(name[1])
print(name[6:])
print(name[::-1])

# Booleans- List, Tuples, Sets are false only when empty, same for strings "", and 0 and yup, False

book1_read = True
book2_read = False

book_read = any([book1_read, book2_read])
print(book_read) #True

all_books_read = all([book1_read,book2_read])
print(all_books_read)

# Number Data Types

# complex_no = 2+3j
num = complex(2,3)

print(num.real, num.imag)

# Built-in Functions

print(abs(-4.69))

print(round(4.95))
print(round(6.88,1))

# Enums- To create constants in Python

from enum import Enum

class State(Enum):
    INACTIVE = 0
    ACTIVE = 1

print(State.ACTIVE.value) # 1
print(State(1)) # State.ACTIVE

print(list(State))
print(len(State))  # 2

# Lists

todos = ["Workout", "Live Session", "Warm Up Resources", "Python Refresher", 4]

print(4 in todos)
print(todos[0])

todos[0] = "Cardio" # List is mutable, unlike tuple
print(todos)

print(todos[1:5:])
print(todos[-1])

todos.append("Projects") # item added at end of list
print(len(todos))
print(todos)

todos.extend(["All notes"]) # adds list to the list
# same as todos += ["All notes"]
print(todos)

todos.remove(4)
print(todos)

print(todos.pop())  # removes last element from the list and shows it here
print(todos)

# Adding items to a list

todos.insert(4,"Test")
print(todos)

todos[1:1] = ["Test1","Test2"] # Adding multiple items at an index
print(todos)


print(sorted(todos)) # It doesn't modify the list

print(todos)

todos.sort()  # sorts uppercase letters first, then lowercase letters
# Also, sorting method modifies original list content
print(todos)

