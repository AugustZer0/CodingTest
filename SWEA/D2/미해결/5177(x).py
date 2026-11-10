import heapq

t = int(input())

for test_case in range(1, t + 1):
    n = int(input())
    arr = list(map(int, input().split()))
    h = []
    for x in arr:
        heapq.heappush(h, x)

    h = [0] + h

    total = 0
    i = n // 2
    while i > 0:
        total += h[i]
        i //= 2

    print(f'#{test_case} {total}')