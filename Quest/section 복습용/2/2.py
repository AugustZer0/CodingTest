t = int(input())

for i in range(t):
    n, s, e, k = map(int, input().split())
    arr = list(map(int, input().split()))
    arr = sorted(arr[s-1:e])
    print(f"#{i + 1} {arr[k - 1]}")