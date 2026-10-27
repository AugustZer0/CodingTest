def DFS(L, s, total):
    global cnt
    if L == k:
        if total % m == 0:
            cnt += 1
    else:
        for i in range(s, n):
            DFS(L + 1, i + 1, total + arr[i])

if __name__ == "__main__":
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    m = int(input())
    cnt = 0
    DFS(0, 0, 0)
    print(cnt)

"""
from itertools import combinations

n, k = map(int, input().split())
arr = list(map(int, input().split()))
m = int(input())
cnt = 0


for comb in combinations(arr, k):
    if sum(comb) % m == 0:
        cnt += 1

print(cnt)
"""
