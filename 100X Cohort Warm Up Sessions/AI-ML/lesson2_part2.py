# Tuples

names = ("Divya","Ria","Issabella")

print(names[0])
print(names[-1])

print(names.index("Ria"))

print("Pia" in names)

print(names[0:2])

print(sorted(names))

# names[0] = "x" 
# not possible, coz tuple is immutable.


newer_names = names + ("Harry","Sheldon")
print(newer_names)

# Dictionaries

me = { "name": "Divya", "age":20, "course":"MTECH" }

print(me["name"])

me["name"] = "Ria"
print(me)

print(me.get("name"))
print(me.get("field","dev"))  # setting a default value in the other parameter, used when the 1st param isn't there in the dictionary

# print(me.pop()) # unlike lists, we need to reference the element here we want to be deleted for pop method.

print(me.pop("age"))
print(me)

print(me.popitem())
print(me)  # works same as pop() works for lists

me["hackathons_won"] = 4
me["hackathons_participated"] = 20
print(me)

print(me.keys())
print(me.values())
print("name" in me)

print(list(me.keys()))

print(me.items())  # dict_items([('name', 'Ria'), ('hackathons_won', 4), ('hackathons_participated', 20)])
print(list(me.items()))  # [('name', 'Ria'), ('hackathons_won', 4), ('hackathons_participated', 20)]

print(len(me))

del me["hackathons_participated"]
print(me)

me_clone = me.copy()
print(me_clone)

# Sets - Unordered & items not repeated, unlike lists

set1 = {"Salad","Milk","Green Tea","Green Coffee"}
set2 = {"Black Coffee", "Cold Coffee","Green Coffee", "Milk Coffee"}

intersect = set1 & set2
print(intersect)

union = set1 | set2
print(union)

difference = set1 - set2
print(difference)

print(set1 > set2) # if true, it would mean set2 is subset of set1. Will return False here.

print("Cold Drink" in set1)
print(len(set1))

# Functions

def greeting(name): # name is a parameter here
    return f"Hello {name}"

print(greeting("Divya"))  # The name "Divya" is an argument here.


# Default values, used when function called without any parameters/all needed parameters.

def greeting(name="dear darling!"):
    return f"Hello {name}"

print(greeting("Divya"))  # Hello Divya
print(greeting())         # Hello dear darling!

# Multiple Parameters

def compliment(name, interest, nation, rel="friend"):
    print(f"Dear {name}, with interests in the invigorating field of {interest}, my dear {rel} from {nation}, I welcome you here!")

compliment("Divya", "Development", "India",)

# Variable Scope

age = 8  # Global Variable

def test():
    print(age)

print(age)
test()

# but if it's a local variable only

def test():
    age = 8
    print(age)

# print(age) # wrong- age isn't even defined here
test()


# Nested Functions

def lower(phrase):
    def lowercase(words):   # local function inside the function, not used anywhere else in the application/program.
        return words.lower()
    
    return lowercase(phrase)

print(lower("Divya is trynna be complicated, BUT IT'S KINDA Really HARD."))

# nonlocal- use this keyword when you've like 2 versions of the value, but u wanna use tge global/non-local one.

def count():
    count = 0

    def increment():
        nonlocal count # wouldn't have worked if this keyword wasn't here
        count += 1
        print(count)

    increment()

count()

# Closures

def counter():
    count = 0

    def increment():
        nonlocal count
        count += 1
        return count
    return increment

increment = counter() # called once, global variable count is obtained

print(increment()) # 1 # local function called multiple times, gets executed, with only the local function running, hence the global variable isn't reset.
print(increment()) # 2
print(increment()) # 3

# Objects

age = 8

print(age.real) # 8
print(age.imag) # 0
print(age.bit_length())  # 4

# all these methods, and there are many more, just for an int object.

# Methods available for an object depends on its type of value( int, list, str, dict, set, tuple, etc)

# Loops- While & For loops

items = ["Juice", "Milk","Tea","Coffee"]

for item in items:
    print(item)

for i in range(15):  # prints 0-14
    print(i)


# Enumerate

items = ["Divya", "Coffee", "Tea", "Milk"]
for index,item in enumerate(items):
    print(index,item)

# Break and Continue

for item in items:
    if item == "Divya":
        print("Divya'a a human being, not an item")
        continue
    print(item) 

"""
Above code will return this:- 

Divya'a a human being, not an item
Coffee
Tea
Milk

"""

items = ["Coffee", "Divya", "Tea", "Milk"]
for item in items:
    if item == "Divya":
        print("Divya's a human, not an item!")
        break
    print(item)

"""

Above code will print this:-

Coffee
Divya's a human, not an item!

"""