def DFS(L, s, time):
    global res
    if time > m:
        return
    if L == n:
        if s > res:
            res = s
    else:
        DFS(L + 1, s+pv[L], time + pt[L])
        DFS(L + 1, s, time)



if __name__ == "__main__":
    n, m = map(int, input().split())
    pv = list()
    pt = list()
    for _ in range(n):
        x, y = map(int, input().split())
        pv.append(x)
        pt.append(y)
    res = -float('inf')
    DFS(0, 0, 0)
    print(res)