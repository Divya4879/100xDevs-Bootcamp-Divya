# Classes

class Acquaintance:
    def like(self):
        print("2-6")

class Friend(Acquaintance):  # Inheritence
    def __init__(self,name,age):   # Used to initialize property of the class
        self.name = name
        self.age = age
    def progress(self):     # Methods of class
        print("Congrats buddy!")  

Harry = Friend("Harry",20) # instantiating a new object from the class

print(type(Harry)) # <class '__main__.Friend'>
print(Harry.name)
print(Harry.age)
Harry.progress()
Harry.like()

# Modules

"""

import game1

game1.get_choices()

"""

# OR

from lesson2_part2 import compliment  # importing just this function from that file

compliment("Divya", "Development", "India",)

from lib import module_example as mod_ex

mod_ex.lower("Divya is trynna be complicated, BUT IT'S KINDA Really HARD.")

# OR

from lib.module_example import lower

print(lower("Divya is trynna be complicated, BUT IT'S KINDA Really HARD."))

"""

SOME PYTHON COMMON UTILITIES/LIBRARIES

math
re- Regular Expressions
json
datetime
sqlite3
os
random
statistics
requests- http network requests
http- create HTTP servers
urllib- to manage URLs

EXAMPLE

"""

from math import sqrt

print(sqrt(8100))  # 90.0

# Arguments from Command Line

# python lesson2_part3.py - Running a python file/executing it
# OR py lesson2_part3.py

