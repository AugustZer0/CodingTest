def DFS(v):
    global cnt
    if v == m:
        for j in range(m):
            print(res[j], end=' ')
        print()
        cnt += 1
    else:
        for i in range(n):
            res[v] = i + 1
            DFS(v + 1)

if __name__ == "__main__":
    n, m = map(int, input().split())
    cnt = 0
    res = [0] * m
    DFS(0)
    print(cnt)