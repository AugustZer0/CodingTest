import sys

def DFS(L, s):
    # 모든 트리를 다 타고, s 가 f일때,
    if L == n and s == f:
        # p에 담아둔 순열 호출
        for x in p:
            print(x, end=' ')
        # 맞다면 시스템 종료, 한줄만 뽑기위해
        sys.exit(0)
    else:
        for i in range(1, n + 1):
            # 순열 중복 방지
            if ch[i] == 0:
                ch[i] = 1
                # 순열 저장
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