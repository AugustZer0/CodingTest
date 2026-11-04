def DFS(L, s):
    global cnt
    if s > T:
        return
    if L == K:
        if s == T:
            cnt += 1
    else:
        for i in range(cn[L] + 1):
            DFS(L + 1, s + (cv[L] * i))

if __name__ == "__main__":
    T = int(input())
    K = int(input())
    cv = list()
    cn = list()
    for _ in range(K):
        a, b = map(int, input().split())
        cv.append(a)
        cn.append(b)
    cnt = 0
    DFS(0, 0)
    print(cnt)