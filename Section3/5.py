from collections import Counter

n, m = map(int, input().split())
cnt = [0] * (n + m + 1)
max_val = 0

for x in range(1, n + 1):
    for y in range(1, m + 1):
        cnt[x + y] += 1

for i in range(m+n+1):
    max_val = max(max_val, cnt[i])

for i in range(n+m+1):
    if cnt[i] == max_val:
        print(i, end= ' ')

    """
    
    """