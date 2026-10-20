import heapq as hq

a = []

while True:
    s = int(input())
    if s == -1:
        break
    if s == 0:
        if len(a) == 0:
            print(-1)
        else:
            print(hq.heappop(a))
    else:
        hq.heappush(a, s)
