# (A) Print Array In Reverse

a=input()

b=input().split(' ')
b=list(map(int,b))

b=b[::-1]

for x in b:
    if x==b[-1]:
        print(x,end='')
    else:
        print(x,end=' ')

'''
Input
5
1 2 3 4 5

Output
5 4 3 2 1
'''

# (B) Sum of Array

a= input()
b=input().split(' ')

b=list(map(int,b))

print(sum(b))

'''
Input
5
1 2 3 4 5

Output
15
'''

# (C) Minimum Element and Its Position

n = int(input())
arr=input().split(' ')


arr_int = list(map(int, arr))

min=min(arr_int)
idx=arr_int.index(min)+1

print(min,idx)

'''
Input
6
7 3 4 5 3 10

Output
3 2
'''

# (D) Maximum Element with Position

n = int(input())
arr=input().split(' ')

arr_int = list(map(int, arr))

max=max(arr_int)
idx=arr_int.index(max)+1

print(max,idx)

'''
Input
5
1 2 4 3 1

Output
4 3
'''

# (E) Search Element in Array

a,b=input().split(' ')


arr=input().split(' ')

if b in arr:
    print("YES")
else:
    print("NO")

'''
Input
5 7
1 7 5 3 2

Output
YES

****************

Input
4 2
1 4 3 7

Output
NO
'''

# (F) Count Occurrences

a,b=input().split(' ')

arr=input().split(' ')

print(arr.count(b))

'''
Input
6 3
1 5 2 3 7 3

Output
2
'''

# (G) Check If Array is Sorted

a= input()
b=input().split(' ')

b=list(map(int,b))

if b==sorted(b):
    print("YES")
else:
    print("NO")

'''
Input
4
5 3 4 1

Output
NO
'''

# (H) Sort 01

count=int(input())

while count>0:
    a=input()
    
    b = input().split(' ')
    b=sorted(list(map(int,b)))
    
    for idx,x in enumerate(b):
        if idx==len(b)-1:
            print(x,end='')
        else:
            print(x,end=' ')
    print()
    
    count-=1

'''
Input
2
8
1 0 1 1 0 1 0 1
5
0 1 0 1 0

Output
0 0 0 1 1 1 1 1
0 0 0 1 1
'''

# (I) Reverse 

a=int(input())

b=input().split()
b=list(map(int,b))

b=b[::-1]

for idx,x in enumerate(b):
    if idx==a:
        print(x,end='')
    else:
        print(x,end=' ')

'''
Input
5
1 3 7 9 10

Output
10 9 7 3 1 
'''