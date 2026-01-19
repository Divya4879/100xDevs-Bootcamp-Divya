# Problem 1

def hello():
    return "Hello World"
    
print(hello());

# Problem 2

def print_first_five():
    print("A","B","C","D","E", sep="\n")
    
print_first_five()

# Problem 3

def print_triangle():
    n = 5
    for i in range(1, n+1):
        print("*" * n)
        n-= 1

print_triangle()

# Problem 4

for i in range(1,6):
    if i == 1 or i == 5:
        print("*" * 5)
    else:
        n = 6-i
        print(" " * (4-i), "*")

# Problem 5

def print_table(n):
    for i in range(1,11):
        print(f"{n} * {i} = {n * i}")
        
print_table(5)

# Problem 6

length,breadth = input().split(" ")

length = int(length)
breadth = int(breadth)

def rect(length, breadth):
    area = length * breadth
    peri = 2 * (length + breadth)
    return area, peri
    
    
area, peri = rect(length, breadth)
print(f"Area = {area}\nPerimeter = {peri}")

# Problem 7

no = int(input())

def multiple(n):
    for i in range(1,11):
        print(f"{n} * {i} = {n * i}")
        
        
multiple(no)

# Problem 8

a, b = input().split()
a = int(a)
b = int(b)

def calc(a, b):
    print(f"{a} + {b} = {a + b}")
    print(f"{a} - {b} = {a - b}")
    print(f"{a} * {b} = {a * b}")
    print(f"{a} / {b} = {a // b}")
    print(f"{a} % {b} = {a % b}")

calc(a, b)

# Problem 8-2

a = int(input())
b = int(input())


print(f"{a} + {b} = {a + b}\n")
print(f"{a} - {b} = {a - b}\n")
print(f"{a} * {b} = {a * b}\n")
print(f"{a} / {b} = {a // b}\n")
print(f"{a} % {b} = {a % b}\n")

# Problem 9

a, b = input().split(" ")

def add_last_digits(a, b):
    return int(a[-1]) + int(b[-1])
    
print(add_last_digits(a,b))

# Problem 10

no = int(input())

def even_odd(no):
    if no % 2 == 0:
        print("Even")
    else:
        print("Odd")
    
even_odd(no)

# Problem 11

a, b = input().split(" ")

a = int(a)
b = int(b)

def fact(a, b):
    if a % b == 0:
        print("Yes")
    else:
        print("No")
        
fact(a, b)

# Problem 12

a, b = input().split(" ")

a = int(a)
b = int(b)

def multiple(a,b):
    if b % a == 0:
        print("Yes")
        
    else:
        print("No")
    
multiple(a,b)

# Problem 13

marks = int(input())

def pass_fail(marks):
    if marks >= 35:
        print("Pass")
    else:
        print("Fail")
        
pass_fail(marks)

# Problem 14

a, b = input().split(" ")

a = int(a)
b = int(b)

def min_max(a,b):
    if a > b:
        min = b
        max = a
    else:
        min = a
        max = b
    return min, max
    
min, max = min_max(a,b)

print(f"Min = {min}\nMax = {max}")

# Problem 15

a, b, c = input().split(" ")

a = int(a)
b = int(b)
c = int(c)

def min_max(a,b,c):
    if a > b and a > c:
        max = a
        if b > c:
            min = c
        else:
            min = b
    elif b > c and b > a:
        max = b
        if a > c:
            min = c
        else:
            min = a
    elif c > a and c > b:
        max = c
        if a > b:
            min = b
        else:
            min = a
            
    return min, max
    
min, max = min_max(a,b,c)

print(f"Min = {min}\nMax = {max}")


# Problem 16

marks = int(input())

def student_eval(marks):
    if marks > 90:
        print("Excellent")
    elif marks in range(81,91):
        print("Good")
    elif marks in range(71,81):
        print("Fair")
    elif marks in range(61,71):
        print("Meets Expectations")
    else:
        print("Below Par")
        
student_eval(marks)


# Problem 17

a, b = input().split()

a = int(a)
b = int(b)


def origin(x, y):
    if x == 0 and y == 0:
        print("Origin")
    elif y == 0:
        print("X axis")
    elif x == 0:
        print("Y axis")
    elif x > 0 and y > 0:
        print("1st Quadrant")
    elif x < 0 and y > 0:
        print("2nd Quadrant")
    elif x < 0 and y < 0:
        print("3rd Quadrant")
    else:
        print("4th Quadrant")
        
origin(a, b)