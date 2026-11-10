for i in range(1, 11):
    t = int(input())
    arr = list(map(int, input().split()))
    cnt = 0

    for j in range(2, t - 2):
        v = min(arr[j] - arr[j - 2], arr[j] - arr[j - 1], arr[j] - arr[j + 1], arr[j] - arr[j + 2])
        if v > 0:
            cnt += v
    print(f"#{i} {cnt}")
    cnt = 0

