from itertools import permutations

n, m = map(int, input().split())
cnt = 0
for perm in permutations(range(1, n + 1), m):
    print(*perm)
    cnt += 1
print(cnt)