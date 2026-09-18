def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

a = int(input())
print(f"결과: {factorial(a)}")