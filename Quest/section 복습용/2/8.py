def reverse(x):
    return x[::-1]

def isPrime(x):
    if x < 2:
        return False
    for i in range(2, int((x ** 0.5) + 1)):
        if x % i == 0:
            return False
    return True

n = int(input())
arr = input().split()

for x in arr:
    res = int(reverse(x))
    if isPrime(res):
        print(res, end=" ")