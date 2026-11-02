def DFS(L, s):
    global res
    if L == n + 1:
        if s > res:
            res = s
    else:
        if L + T[L] <= n + 1:
            DFS(L + T[L], s + P[L])
        DFS(L + 1, s)

if __name__ == "__main__":
    n = int(input())
    T = list()
    P = list()
    for _ in range(n):
        a, b = map(int, input().split())
        T.append(a)
        P.append(b)
    res = -float('inf')
    T.insert(0, 0)
    P.insert(0, 0)
    DFS(1, 0)
    print(res)