def DFS(L, s, t):
    global cnt

    if t > k:
        return

    if L == len(arr):
        if s == n:
            if t == k:
                cnt += 1
    else:
        DFS(L + 1, s + 1, t + arr[L])
        DFS(L + 1, s, t)


t = int(input())
arr = [i for i in range(1, 13)]

for test_case in range(1, t + 1):
    n, k = map(int, input().split())
    cnt = 0
    DFS(0, 0, 0)
    print(f"#{test_case} {cnt}")