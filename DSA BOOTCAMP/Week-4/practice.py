# Max element

# n=int(input())
# arr=list(map(int, input().split()))

# max=arr[0]

# for i in arr:
#     if i>max:
#         max=i
    
# print(max)

'''
Input:- 
6
1 4 8 7 9 3

Output:-
9
'''

# Count of element

# n,target=map(int,input().split())
# arr=list(map(int,input().split()))

# count=0

# for i in arr:
#     if i==target:
#         count+=1

# print(count)

'''
Input:-
6 8
7 6 8 3 7 8 9 8 8

Output:-
4
'''

# Find if array is sorted

# n=int(input())
# arr=list(map(int,input().split()))

# is_sorted=True

# for a in range(1,n):
#     if arr[a-1]>arr[a]:
#         is_sorted=False
#         break

# print("YES" if is_sorted else "NO")

'''
Input:-
4
3 5 7 8 

Output:-
True
****************

Input:-
6
2 2 5 7 4 8

Output:-
False
'''

# Swap alternate elements

# n=int(input())
# arr=list(map(int,input().split()))

# arr1=arr.copy()

# for i in range(n):
#     if i%2==0 and i<n-1:
#         arr[i]=arr1[i+1]
#     elif i%2==1:
#             arr[i]=arr1[i-1]

# print(*arr)

'''
Input:-
6
5 7 8 9 3 2

Output:-
7 5 9 8 2 3

******************

Input:-
5
7 8 1 2 4

Output:-
8 7 2 1 4
'''

# Missing Number

# n=int(input())
# arr=list(map(int, input().split()))

# for i in set(arr):
#     if arr.count(i)==1:
#         print(i)
#         break


# Find HCF

# def factors(n):
#     arr=[]
#     for i in range(2,n+1):
#         if n%i==0:
#             arr.append(i)
#     return arr


# a,b=map(int,input().split())

# def find_hcf(a,b):
#     arr1=factors(a)
#     arr2=factors(b)
    
#     common_factors=list(set(arr1).intersection(set(arr2)))
#     if common_factors==[]:
#         return []        
#     print(max(common_factors))

# find_hcf(a,b)