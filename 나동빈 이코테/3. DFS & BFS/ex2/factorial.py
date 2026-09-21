"""
마지막에 return 1이 되어 답이 1이 나올거 같지만 아님
밑에 있는 return이 덮어쓰는줄도 알았는데 그것도 아님
결론은 n이 1까지 내려가면서 return 1을 실행시키고, factorial 1이 1을 반환 2가 2를 반환 3이 6을 반환하는식으로 올라가짐 -> Call Stack
"""
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)


print(factorial(5))