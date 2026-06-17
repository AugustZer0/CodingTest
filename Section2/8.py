import math

def reverse(x):
    return x[::-1]

def isPrime(x):
    if x <= 1:
        return False
    
    for i in range(2, int(math.sqrt(x) + 1)):
        if x % i == 0:
            return False
    return x
        

n = int(input())
a = list(input().split())


for i in a:
    reverse_num = int(reverse(i))
    result = isPrime(reverse_num)
    
    if result != False:
        print(result, end = ' ')