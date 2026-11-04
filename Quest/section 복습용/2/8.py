def reverse(x):
    return x[::-1]

def isPrime(x):
    if x < 2:
        return False
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True

if __name__ == "__main__":
    n = int(input())
    arr = list(input().split())

    for i in arr:
        num = int(reverse(i))
        if isPrime(num):
            print(num, end=' ')