t = int(input())

for i in range(1, t + 1):
    n, s, e, k = map(int, input().split())
    arr = list(map(int, input().split()))

    arr = sorted(arr[s-1:e])
    print(f"#{i} {arr[k-1]}")