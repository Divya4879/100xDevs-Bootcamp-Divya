# (A) Print 1 to N

i = int(input())

for i in range(1,i+1):
    print(i)



# (B) Print N to 1

i = int(input())
i1 = []

def decreasing(i):
    for i in range(i,0,-1):
        i1.append(i)
        
decreasing(i)
    
for _ in i1:
    print(_, end=" ")



# (C) Print All Even Numbers from 1 to N

i = int(input())
i1 = []

def even_list(i):
    for i in range(1,i+1):
        if i%2==0:
            i1.append(i)
            
even_list(i)

for _ in i1:
    print(_,end=" ")



# (D) Print from L to R

a, b  = input().split(" ")

a= int(a)
b = int(b)

for i in range(a,b+1):
    print(i,end=" ")


# (E) Print All Uppercase Alphabets

import string

string = string.ascii_uppercase

for i in string:
    print(i,end=" ")


# (F) Print Table of N

i = int(input())

for n in range(1,11):
    print(f"{i} * {n} = {i*n}")


# (G) Count Numbers

i = int(input())
a = list(input().split(" "))
a1 = []

for n in a:
    a1.append(int(n))
    

pos = 0
neg = 0
even = 0
odd = 0

for _ in a1:
    if _%2==0:
        even += 1
    else: 
        odd += 1
    if _>0:
        pos += 1
    if _<0:
        neg += 1
        
print(pos,neg,even,odd,sep="\n")


# (H) Sum of First N Natural Numbers

i = int(input())
sum = 0

for _ in range(1,i+1):
    sum += _
    
print(sum)


# (I) Factorial

i = int(input())
product = 1

for _ in range(1,i+1):
    product *= _
    
print(product)


# (J) $x^n$

a, b = input().split()

a = int(a)
b = int(b)

print(a ** b)


#  (K) Print Number in Reverse

i = input()

a = i[::-1]

print(a)


# (L) Sum Of Digits

n = list(input())
sum = 0

for _ in n:
    sum += int(_)

print(sum)


# (M) Reverse Number and Store in a Variable

i = input()

a = int(i[::-1])

print(a)


# (N) Palindrome

i = input()


a = int(i[::-1])
i = int(i)

if a==i:
    print("YES")
else:
    print("NO")
