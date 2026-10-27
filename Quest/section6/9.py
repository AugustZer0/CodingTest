import sys

def DFS(L, s):
    if L == n and s == f:
        for x in p:
            print(x, end=' ')
        sys.exit(0)
    else:
        for i in range(1, n + 1):
            if ch[i] == 0:
                ch[i] = 1
                p[L] = i
                DFS(L + 1, s + (p[L] * b[L]))
                ch[i] = 0

if __name__ == "__main__":
    n, f = map(int, input().split())

    # p = 순열 저장, b = 이항 계수 저장, ch = 순열 만들 때 중복 방지
    p = [0] * n
    b = [1] * n
    ch = [0] * (n + 1)
    for i in range(1, n):
        b[i] = b[i - 1] * (n - i) // i
    DFS(0, 0)

"""
from itertools import permutations

n, f = map(int, input().split())
b= [1] * n

for i in range(1, n):
    b[i] = b[i - 1] * (n - i) // i

for perm in permutations(range(1, n + 1)):
    s = 0
    for L, x in enumerate(perm):
        s += (x * b[L])
    if s == f:
        print(*perm)
        break
"""