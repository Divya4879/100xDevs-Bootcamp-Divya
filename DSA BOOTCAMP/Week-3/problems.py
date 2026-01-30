# Problem 1 - Hello Functions

n = int(input())

def hello(n):
    for i in range(n):
        print("I am learning functions")
    
hello(n)

'''
Input
3

Output
I am learning functions
I am learning functions
I am learning functions
'''


# Problem 2- Print Factors - I

n = int(input())

def factors(n):
    for i in range(1,n+1):
        if n%i==0:
            print(i,end=" ")
            
factors(n)
    
'''
Input
12

Output
1 2 3 4 6 12 
'''


# Problem 3- Print Factors - II

n = int(input())

def factors(n):
    for i in range(n,0,-1):
        if n%i==0:
            print(i,end=" ")
            
factors(n)

'''
Input
12

Output
12 6 4 3 2 1 
'''


# Problem 4- Check Prime

n = int(input())
is_prime= True

def prime(n):
    if n==1:
        print("Not Prime")
        return
    for i in range(2,n):
        if n%i==0:
            is_prime= False
            print("Not Prime")
            return
            
    print("Prime")
    
prime(n)

'''
Input
17

Output
Prime
'''


# Problem 5- Factorial

n = int(input())

def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)
        
print(factorial(n))

'''
Input
5

Output
120
'''

# Problem 6- nCr

n,r= input().split(" ")
n =int(n)
r= int(r)

def fact(a):
    if a==0:
        return 1
    else:
        return a*fact(a-1)
        

def combination(n,r):
    return fact(n)//(fact(r)*fact(n-r))
    
print(combination(n,r))


'''
Input
5 2

Output
10
'''


# Problem 7- Print Primes from 1 to N

n = int(input())
primes_list=[]

def is_prime(n):
    if n==1:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True
        
def primes(n):
    for i in range(1,n+1):
        if is_prime(i):
            primes_list.append(i)
    return primes_list
            
primes_list= primes(n)

for i in range(len(primes_list)):
    if i==len(primes_list)-1:
        print(primes_list[i],end="")
    else:
        print(primes_list[i],end=" ")

'''
Input
13

Output
2 3 5 7 11 13
'''


# Problem 8- Count Zeroes

n = input()

def count_zeroes(n):
    count=0
    for i in n:
        if i == "0":
            count+=1
    return count
    
print(count_zeroes(n))

'''
Input
102030

Output
3
'''


# Problem 9- Find HCF

a,b = input().split(" ")
a = int(a)
b= int(b)


def factors(x):
    factors_hcf=set()
    for i in range(2,x):
        if x%i==0:
            factors_hcf.add(i)
    return factors_hcf
   

def hcf(a,b):
    if b%a==0:
        return a
    else:
        facts1= factors(a)
        facts2= factors(b)
        facts= facts1 & facts2
        if facts:
            return max(facts)
        else:
            return 1
        
print(hcf(a,b))

'''
Input
12 36

Output
12
'''