def DFS(L):
    global cnt
    if L == m:
        for j in range(m):
            print(result[j], end=' ')
        print()
        cnt += 1
    else:
        for i in range(1, n + 1):
            result[L] = i
            DFS(L + 1)

if __name__ == "__main__":
    n, m = map(int, input().split())
    result = [0] * m
    cnt = 0
    DFS(0)
    print(cnt)


# 라이브러리를 사용해서 해결
"""
from itertools import product

n, m = map(int, input().split())

for i in product(range(1, n + 1), repeat = m):
    print(*i)

print(n ** m)
"""