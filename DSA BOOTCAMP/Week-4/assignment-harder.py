# (J) Arrange the Numbers

count=int(input())

while count>0:
    a= int(input())
    if a%2==0:
        a1=a2=a//2
    else:
        a1=(a+1)//2
        a2=(a-1)//2
    
    def first_half(a1):
        x1=[]
        x1+=list(range(1,2*a1,2))
        return x1
    
    def second_half(a2):
        x2=[]
        x2+=list(range(2,2*a2+1,2))
        x2=x2[::-1]
        return x2
    
    res=list(first_half(a1))+list(second_half(a2))
    
    for idx,x in enumerate(res):
        print(x,end=' ')
    print()
    
    
    count-=1

'''
Input:-
3
6
7
8

Output:-
1 3 5 6 4 2 
1 3 5 7 6 4 2 
1 3 5 7 8 6 4 2 
'''

# (K) Swap Alternate

t = int(input())

while t > 0:
    n = int(input())
    if n == 0:
        print()
        t -= 1
        continue
    arr = list(map(int, input().split()))

    for i in range(0, n-1, 2):
        arr[i], arr[i+1] = arr[i+1], arr[i]

    print(*arr)
    t -= 1

'''
Input:-
2
9
9 3 6 12 4 32 5 11 19
4
1 2 3 4

Output:-
3 9 12 6 32 4 11 5 19
2 1 4 3
'''

# (L) Missing Number

count=int(input())

while count>0:
    a=input()
    
    b=input().split(' ')
    b=list(map(int,b))
    
    unique=[]
    
    for x in b:
        if x in unique:
            unique.remove(x)
        else:
            unique.append(x)
            
    print(unique[0])
    
    count-=1

'''
Input:-
2
5
2 4 7 2 7
9
1 3 1 3 6 6 7 10 7

Output:-
4
10
'''

# (M) Find Duplicate Number

count=int(input())

while count>0:
    a=input()
    
    b=input().split(' ')
    b=list(map(int,b))
    
    for x in set(b):
        b.remove(x)
            
    print(b[0])
    
    count-=1

'''
Input:-
2
5
0 2 1 3 1
7
0 3 1 5 4 3 2

Output:-
1
3
'''

# (N) Intersection of Arrays

t= int(input())


while t>0:
    res=[]
    n1=int(input())
    if n1==0:
        arr1=[]
    else:
        arr1=list(map(int,input().split()))
    
    n2=int(input())
    if n2==0:
        arr2=[]
    else:
        arr2=list(map(int,input().split()))
        
    freq={}
    for num in arr2:
        freq[num]=arr2.count(num)
        
    for num in arr1:
        if num in freq.keys() and freq[num]>0:
            res.append(num)
            freq[num]-=1
            
    print(*res)
    t-=1

'''
Input:-
2
6
2 6 8 5 4 3
4
2 3 4 7
2
10 10
1
10

Output:-
2 4 3
10
'''

# (O) Pair Sum

t= int(input())

while t>0:
    n=int(input())
    arr=list(map(int,input().split(' ')))
    
    if n<2:
        pairs=0
        
    else:
        
        pairs=0
        
        sum=int(input())
        
        for num in range(n):
            for i in range(num+1,n):
                if arr[num]+arr[i]==sum:
                    pairs+=1
                
    print(pairs)
    t-=1

'''
Input:-
2
9
1 3 6 2 5 4 3 2 4
12
6
2 8 10 5 -2 5
10

Output:-
0
2
'''

# (P) Triplets

t= int(input())

while t>0:
    n=int(input())
    if n==0:
        arr=[]
    else:
        arr=list(map(int,input().split()))
    sum=int(input())
    count=0
    
    
    if n<3:
        pass
    else:
        for i in range(n):
            for j in range(i+1,n):
                for k in range(j+1,n):
                    if arr[i]+arr[j]+arr[k]==sum:
                        count+=1
                        
    print(count)
    t-=1

'''
Input:-
2
7
1 2 3 4 5 6 7
19
9
2 -5 8 -6 0 5 10 11 -3
10

Output:-
0
5
'''

# (O) Pair Sum

t = int(input())

while t > 0:
    n = int(input())
    if n == 0:
        arr = []
    else:
        arr = list(map(int, input().split()))
    
    X = int(input())

    freq = {}
    count = 0

    for num in arr:
        need = X - num
        # If need is already seen, we can form pairs
        if need in freq:
            count += freq[need]
        # Add current number to freq map
        freq[num] = freq.get(num, 0) + 1

    print(count)
    t -= 1

'''
Input:-
2
9
1 3 6 2 5 4 3 2 4
12
6
2 8 10 5 -2 5
10

Output:-
0
2
'''

# (P) Triplets

t = int(input())

while t > 0:
    n = int(input())
    
    if n == 0:
        arr = []
    else:
        arr = list(map(int, input().split()))
    
    X = int(input())
    
    count = 0
    
    # Only loop if array has at least 3 elements
    if n >= 3:
        for i in range(n):
            for j in range(i+1, n):
                for k in range(j+1, n):
                    if arr[i] + arr[j] + arr[k] == X:
                        count += 1
    
    print(count)
    
    t -= 1

'''
Input:-
2
7
1 2 3 4 5 6 7
19
9
2 -5 8 -6 0 5 10 11 -3
10

Output:-
0
5
'''

# (Q) Count Quadraplets

n, x = map(int, input().split())

arr = list(map(int, input().split()))

count = 0

if n >= 4:
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                for l in range(k+1, n):
                    if arr[i] - 2*arr[j] + 3*arr[k] - 4*arr[l] == x:
                        count += 1

print(count)

'''
Input:-
8 -10
1 2 3 4 5 6 5 6

Output:-
5
'''