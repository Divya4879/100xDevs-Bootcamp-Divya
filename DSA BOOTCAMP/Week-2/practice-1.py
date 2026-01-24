# Print reverse of number

no= int(input())
a=""


while no>=0:
    a+= str(no%10)
    no//=10
    
print(int(a))

# Sum of Digits

no = int(input())
sum = 0

while no>0:
    sum+= no%10
    no//=10
    
print(sum)

# Count Digits

no= int(input())
count=0

while no>0:
    no//=10
    count+=1
    
print(count)

# Palindrome

no = int(input())
a= no
reverse = 0

while no>0:
    reverse*=10
    reverse+= no%10
    no//=10


    
print(a==reverse)

# Numbered rectangle

i = int(input())
j = int(input())

for x in range(1,i+1):
    for y in range(1,j+1):
        print(str(x),end="")
    print()
    
'''

Sample Input
5
7

Your Output
1111111
2222222
3333333
4444444
5555555

'''

# Numbered Rectangle-2

# i = int(input())
# j = int(input())

# for x in range(1,i+1):
#     for y in range(1,j+1):
#         print(y,end="")
#     print()
    
'''

Sample Input
5
7

Your Output
1234567
1234567
1234567
1234567
1234567

'''

# Numbered Rectangle-3

import string

# i = int(input())
# j = int(input())

# for x in range(i):
#     print(string.ascii_uppercase[:j])
    
'''

Sample Input
5
7

Your Output
ABCDEFG
ABCDEFG
ABCDEFG
ABCDEFG
ABCDEFG
        
'''

# Numbered Rectangle-4

# i = int(input())
# j = int(input())

# for x in range(i):
#     print(string.ascii_uppercase[x]*j)
    
'''

Sample Input
5
7

Your Output
AAAAAAA
BBBBBBB
CCCCCCC
DDDDDDD
EEEEEEE

'''

# Binary Pyramid

i = int(input())

for x in range(1,i+1):
    for y in range(1,x+1):
        if x==y or (x+y)%2==0:
            print("0",sep="",end="")
        else:
            print(1,sep="",end="")
        
    print()
    
'''

Sample Input
5

Your Output
0
10
010
1010
01010

'''