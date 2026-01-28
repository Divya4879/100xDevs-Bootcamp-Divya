# Problem 1- Hello Codeforces

'''
i = int(input())

for i in range(1,i+1):
    print(f"Hello Codeforces {i}")
'''

'''

Sample Input:-
8

Sample Output:-
Hello Codeforces 1
Hello Codeforces 2
Hello Codeforces 3
Hello Codeforces 4
Hello Codeforces 5
Hello Codeforces 6
Hello Codeforces 7
Hello Codeforces 8
'''

# Problem 2- Is Vowel?

'''
x = input()

if (x in ["a","e","i","o","u"]):
    print("YES")
else:
    print("NO")
'''

# Problem 3- Second Last Digit

'''
i = input()

print(int(i[-2]))
'''

# Problem 4- Leap Year

'''
yr = int(input())

if yr%100==0:
    if yr%400==0:
        print("Yes")
    else:
        print("No")

elif yr%4==0:
    print("Yes")

else:
    print("No")
'''

# Problem 5- Count Good Numbers- I did it wrong the 1st time.

'''
i = int(input())
 
y = input().split(" ")

y1 = [int(_) for _ in y]

good = 0
 
for x in y1:
    if (x!=0 and 18%x==0) or x%45==0:
        good+=1
 
print(good)
'''

# Problem 6- FizzBuzz

'''
i = int(input())

for x in range(1,i+1):
    if x%3==0 and x%5==0:
        print("FizzBuzz")
    elif x%3==0:
        print("Fizz")
    elif(x%5==0):
        print("Buzz")
    else:
        print(x)
'''

'''

Input- 15

Output-
1
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
11
Fizz
13
14
FizzBuzz
'''

# Problem 7- Count Zeros 

'''
i = input()
count = 0

for x in range(len(i)):
    if i[x]=='0':
        count+=1

print(count)
'''

# Problem 8- Empty Rectangle

'''
a,b= input().split()

a= int(a)
b=int(b)

for row in range(1,a+1):
    for col in range(1,b+1):
        if row==1 or col==1 or row==a or col==b:
            print("^",end="",sep="")
        else:
            print(" ",end="",sep="")
       
    print()
'''

'''

Sample Input: 7 10

Sample Output:-
^^^^^^^^^^
^        ^
^        ^
^        ^
^        ^
^        ^
^^^^^^^^^^

'''

# Problem 9- Shifted Pyramid

'''
i = int(input())

for x in range(1,i+1):
    print(" "*(x-1)+"x"*x)
'''

'''

Sample Input: 10

Sample Output:
x
 xx
  xxx
   xxxx
    xxxxx
     xxxxxx
      xxxxxxx
       xxxxxxxx
        xxxxxxxxx
         xxxxxxxxxx


'''

# Problem 10- Hourglass- Wrong submission firstly, coz of spaces

'''
i = int(input())
 
for a in range(1,i):
    print(" "*(a-1)+". "*(i-a)+".")
 
for a in range(2,i+2):
    print(" "*(i-a+1)+". "*(a-2)+".")
'''

'''
Sample Input:- 10

Sample Output:-
. . . . . . . . . . 
 . . . . . . . . .
  . . . . . . . .
   . . . . . . .
    . . . . . .
     . . . . .
      . . . .
       . . .
        . .
         .
        . .
       . . .
      . . . .
     . . . . .
    . . . . . .
   . . . . . . .
  . . . . . . . .
 . . . . . . . . .
. . . . . . . . . .

'''


# Problem 11:- Arrow:- Good pattern

'''
x = int(input())

for a in range(1,x+1):
    if a==1:
        print(">")
    else:
        print(" "*(a-1)+">"+" "*(2*(a)-3)+">",sep="")

for a in range(x-1,0,-1):
    if a==1:
        print(">")
    else:
        print(" "*(a-1)+">"+" "*(2*(a)-3)+">",sep="")
'''

'''
Sample Input:- 10

Sample Output:-
>
 > >
  >   >
   >     >
    >       >
     >         >
      >           >
       >             >
        >               >
         >                 >
        >               >
       >             >
      >           >
     >         >
    >       >
   >     >
  >   >
 > >
>
'''

