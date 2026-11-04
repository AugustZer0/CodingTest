n = int(input())
arr = list(map(int, input().split()))
avg = int(sum(arr) / n + 0.5)

minn = float('inf')
ix = 0

for idx, value in enumerate(arr):
    tmp = abs(value - avg)
    if tmp < minn:
        minn = tmp
        ix = idx
    elif tmp == minn and value > arr[ix]:
            ix = idx

print(avg, ix + 1)

