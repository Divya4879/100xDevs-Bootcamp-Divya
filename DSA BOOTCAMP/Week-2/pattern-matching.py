# (A) 2-Stars

i = int(input())

for i in range(i):
    print("**")



# (B) M-Stars

a,b = input().split()
a = int(a)
b = int(b)

for i in range(a):
    print("*" * b)


# (C) Pyramid

a = int(input())


for i in range(1,a+1):
    print("*" * i)



# (D) Inverse Pyramid

a = int(input())


for i in range(a,0,-1):
    print("*" * i)



# (E) Square

i = int(input())

for _ in range(1,i+1):
    print("*" * i)



# (F) Hollow Square

i = int(input())
j = i

for x in range(1,i+1):
    for y in range(1,j+1):
        if x==1 or x==i or y==1 or y ==j:
            print("*",end="")
        else:
            print(" ",end="")
    print()



# (G) Hollow Rectangle

i,j = input().split()
i = int(i)
j = int(j)

for x in range(1,i+1):
    for y in range(1,j+1):
        if x==1 or x==i or y==1 or y ==j:
            print("*",end="")
        else:
            print(" ",end="")
    print()



# (H) Triangle

n = int(input())

# for a in range(1, n+1):
#     print(" "*(n-a), "* "*a)

for i in range(1, n + 1):
    print(" " * (n - i) + "* " * (i - 1) + "*")



# (I) Hollow Triangle

i = int(input())

rows = i
cols = 2*i-1

for row in range(rows):
    for col in range(cols):
        if (row==rows-1 and col%2==0) or row+col==rows-1 or col-row==rows-1:
            print("*",end="",sep="")
        else:
            print(" ",end="",sep="")
    print()



#  (J) Inverted Hollow Triangle

i = int(input())

rows = i
cols = 2*i-1


for row in range(rows):
    for col in range(cols):
        if (row==0 and col%2==0)  or row==col or row+col==cols-1:
            print("*",end="",sep="")
        else:
            print(" ",end="",sep="")
    print()



# (K) Diamond

n = int(input())

for row in range(1, n + 1):
    print(" " * (n - row) + "* " * (row - 1) + "*")

for row in range(n - 1, 0, -1):
    print(" " * (n - row) + "* " * (row - 1) + "*")



# (L) Hollow Diamond

i = int(input())

for x in range(2*i-1):
    for y in range(2*i-1):
        if x+y+1==i or y-x+1==i or x-y+1==i or (x+y)/3+1==i:
            print("*",sep="",end="")
        else:
            print(" ",sep="",end="")
    print()




# (M) Inverted Diamond

'''
***** *****
****   ****
***     ***
**       **
*         *
**       **
***     ***
****   ****
***** *****


'''

i = int(input())

for x in range(i):
    print("*"*(i-x)," "*(2*x+1),"*"*(i-x),sep="")
    
for x in range(2,i+1):
    if x==i:
        print("*"*x," ","*"*x,sep="")
    else:
        print("*"*x," "*((2*(i-x))-1),"*"*x)



# (N) Crown

'''
*            *
**          **
***        ***
****      ****
*****    *****
******  ******
**************

'''

i =int(input())

for x in range(1,i+1):
    for y in range(1,2*i+1):
        if (y==i and x==i-1) or (y-x==1 and x<i and y<i) or (y==i+1 and x<i) or (i+1<=x+y<=2*i and y>x) or (2<=y-x<i and x<i and y<i):
            print(" ",end="",sep="")
        else:
            print("*",end="",sep="")
    print()



# (O) Butterfly


'''
*          *
**        **
***      ***
****    ****
*****  *****
************
*****  *****
****    ****
***      ***
**        **
*          *

'''

i = int(input())

for x in range(1,i):
    print("*"*(x)," "*2*(i-x),"*"*(x),sep="")

for x in range(i,0,-1):
    print("*"*(x)," "*2*(i-x),"*"*(x),sep="")




# (P) Numbered Traingle

n = int(input())


for i in range(1,n+1):
    print(int(str(i)*i))



# (Q) Binary Pyramid

i = int(input())
result = []

for x in range(i):
    for y in range(x+1):
        if (x+y)%2==0:
            print(0,end="",sep="")
        else:
            print(1,end="",sep="")
    print()




# (R) Vertical Traingle

i = int(input())

for x in range(2*i-1):
    for y in range(2*i):
        # print(x,y,sep="",end=" ")
        if y==0  or (i>x and x==y) or (x+y==2*i-2 and x>y) or (x>y and x+y<2*i-1):
            print("*",end=" ",sep="")
        
    print()



# (S) Inverted Vertical Triangle


i = int(input())

for x in range(2*i-1):
    for y in range(2*i):
        # print(x,y,sep="",end=" ")
        if y==0  or (i>x and x==y) or (x+y==2*i-2 and x>y):
            print("*",end=" ",sep="")
        else:
            print(" ",end=" ",sep="")
    print()