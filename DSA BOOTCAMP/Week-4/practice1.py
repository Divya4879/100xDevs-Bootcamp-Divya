# Reversing same array

# n=int(input())
# arr=list(map(int,input().split()))

# l,j=0,n-1

# while j>l:
#     arr[l],arr[j]=arr[j],arr[l]
#     l+=1
#     j-=1

# print(*arr)

'''
Input:-
6
2 5 7 8 9 0

Output:-
0 9 8 7 5 2
'''

# Missing Number

n=int(input())
arr=list(map(int,input().split()))

res=0
for a in arr:
    res^=a

print(res)