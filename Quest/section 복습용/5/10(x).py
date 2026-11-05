import heapq as hq

arr = []

while True:
    n = int(input())
    if n == -1:
        break
    elif n == 0:
        print(hq.heappop(arr))
    else:
        hq.heappush(arr, n)