def DFS(L, s):
    global res
    if L == n:
        if 0 < s <= total:
            res.add(s)

    else:
        DFS(L + 1, s + G[L])
        DFS(L + 1, s - G[L])
        DFS(L + 1, s)


if __name__ == "__main__":
    n = int(input())
    G = list(map(int, input().split()))
    total = sum(G)
    res = set()
    DFS(0, 0)
    print(total-len(res))
