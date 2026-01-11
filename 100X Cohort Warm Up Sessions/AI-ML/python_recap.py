print("Divya is a girl", end = "")
print(", obviously.")

print("Divya is a ___", sep=",")

print("Divya", 'Ria', "TechDSA")
print("Divya", 'Ria', "TechDSA", sep=",")

print("\n\n\n\n\n")


def spam():
    global spam
    eggs = "spam"

eggs = "global"
spam()
print(eggs)


a = ["Green Coffee", "Cold Coffee", "Black Coffee", "Milk Coffee"]
b = ["Milk Tea", "Green Tea", "Lemon Tea", "Mint Tea"]

a.sort(reverse=True)
print(a)

print(list(zip(a,b)))   # zip(a,b) - takes 2 lists a & b - same length-returns as a tuple of their tuples, like ((a0,b0),(a1,b1),....(aN,bN))

cat = ['fat', 'orange', 'loud']
size, color, disposition = cat  # assigning all 3 variables to each item of the list at once

a, b = "Divya", "Ria"
a, b = b, a
print(a)


beverages = {"fav": "Milk Tea", "healthy": "Green Tea", "best": "Black Coffee"}

print(f"I like {beverages['fav']} the best, atleast for now, but yup, {beverages.get("fav","Coffee")} is the go-to one for long sessions/learning, when I gotta stay awake.But yup, you know what {beverages.get("universal","water")} has got to be the best one-drink it chilled, add lemons, or lukewarm, or boil it & sip it regularly.")



spam = {"random":"test", "mystery":"PKYEK"}
if "book" not in spam:
    spam["book"] = "HP series"

print(spam)

# OR

spam = {"random":"test", "mystery":"PKYEK"}
spam.setdefault("book","HP Series")  # no need to check then add, this value will be used as default if the key didn't exist in the dictionary.

print(spam["book"])

# Merging dictionaries

a = {'a':1, 'b':2}
b = {'x':5,'y':8, 'z':9, 'b':5}

c = {**a, **b}  # 2nd dict's values are prioritized
print(c)


# Sets - Unordered collection with no duplicate elements
# we can't access them by index nos, coz unordered, so no set1[index_no]

a = {2,5,8,54}

b = set([3,8,6,4,8,2,3])

print(a)
print(b)

a.add(3) # adds 1 element only
print(a)

a.update([45,54, 75,100,98,15])
print(a)

a.remove(2)
print(a)

# a.remove(2) # you'll get an error here

a.discard(2) # works just like remove method, but unlike it, discard() doesn't raise an error if we add a non-existing elemnt to be discarded, unlike the remove()

print(a.union(b))
print(a.intersection(b))
print(a.difference(b))    # a-b
print(b.difference(a))

print(a.symmetric_difference(b))  # returns the elements unique to each set, like A-B and B-A


# List Comprehension

a = [2,5,8]

print([i*2 for i in a])     # [4, 10, 16]



# Set Comprehension

s = {"abc", "def"}
print({i.upper() for i in s}) # {'ABC', 'DEF'}



# Dictionary Comprehension

d = {"name":"Divya", "field":"Dev"}

print({v:k for k,v in d.items()})    # {'Divya': 'name', 'Dev': 'field'}


'''

Common Escape Characters:-

\' - '
\" - "
\t - tab
\n
\\ - \

'''

print(r"Divya is a sweetiepie\!")  # r-string :- it completely ignores the escape characters


'''
Multiline strings
'''

a = "Divya is a techie."

print("techie" in a)
print("Div" in a)
print("Ria" in a)
print("cat" not in a)


# Strings

a = ", ".join(["cat","rat","bat","mat","hat","sat","fat"])
print(a)  # cat, rat, bat, mat, hat, sat, fat

a = " ".join(["cat","rat","bat","mat","hat","sat","fat"])
print(a)  # cat rat bat mat hat sat fat


print("Divya".rjust(10))  #      Divya- Right Justify
print("Divya".rjust(20,"*"))
print("Divya".ljust(20,"-"))

print("Hello".center(20))
print("Hello".center(20,"*"))

'''

OUTPUT:-

     Divya
***************Divya
Divya---------------
       Hello
*******Hello********

'''

# assert keyword- to check it code's working correctly as it needs to

# logging- import logging, for more, read docs.

# Lambda Function

def sum(a, b):
    return a + b

print(sum(7,9))

# OR

sum = lambda a, b: a + b
print(sum(5,90))

# OR

print((lambda x, y: x + y)(2,6))


# Ternary Operator- if else statement in a single line

age = 15
print('kid' if age<18 else 'adult')


# args and kwargs

def fruits(*args):
    for fruit in args:
        print(fruit)

fruits("apples", "bananas", "grapes")

'''

Output:-

apples
bananas
grapes

'''

def fruit(**kargs):
    for key,fruit in kargs.items():
        print(f"{key}:{fruit}")

fruit(fav="Mango",top="Apples")

# Output:-

# fav:Mango
# top:Apples


# if __name__ == "__main__":
#     # execute only if run as a script
#     main()

# Example explaining above piece of code:-

# def add(a,b):
#     return a + b

# print(add(10,20))  # we can test it by calling the function, save it as calculate.py

# Now, if we want to use that modle by importing, we've to comment out our call, instead we
# can write like this in calculate.py

# if __name__ == "__main__":
#     print(add(30,50))

import calculate
calculate.add(40,60)