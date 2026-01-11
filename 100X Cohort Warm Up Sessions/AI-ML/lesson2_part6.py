# Installing Packages with pip

"""
All public/open-source python packages on pypi.org, & can be installed using pip

also, pip used in the terminal only, like pip install requests

also, once a package is installed for 1 file, available for all Python files coz it's installed globally, using pip.

 upgrading a package - pip install -U requests

 uninstalling it - pip uninstall requests

 Some info about an installed package- pip show requests

"""


# List Comprehensions

nums = [1,-3,7,5]  # [1, 9, 49, 25]

nums_squared = [n**2 for n in nums]   # List comprehension
print(nums_squared)



# Polymorphism

class Dog:
    def eat(self):
        print("Eating dog food.")

class Cat:
    def eat(self):
        print("Eating cat food.")

dog = Dog()
cat = Cat()

dog.eat()         # eat()- different functionlities for both classes
cat.eat()


# Operator Overloading

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __gt__(self, other):  ## operator overloading
        return True if self.age > other.age else False
    
roger = Dog("Roger",3)
syd = Dog("Syd",5)

print(roger > syd)

"""

More examples:-

__add__()
__sub__()
__mul__()
__truediv__() - responds to /
__floordiv__() - responds to //
__mod__()
__pow__() - **
__rshift__() - >>
__lshift__()
__and__()
__or__()
__xor__()

"""
