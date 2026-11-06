def DFS(L, s, t):
    global res
    if s + (total - t) < res:
        return

    if s > c:
        return

    if L == n:
        if s > res:
            res = s
    else:
        DFS(L + 1, s + arr[L], t + arr[L])
        DFS(L + 1, s, t + arr[L])

if __name__ == "__main__":
    c, n = map(int, input().split())
    arr = [int(input()) for _ in range(n)]
    total = sum(arr)
    res = -float('inf')
    DFS(0, 0, 0)
    print(res)