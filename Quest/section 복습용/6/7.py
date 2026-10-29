def DFS(L, s):
    global result

    if L > result:
        return

    if s > m:
        return

    if s == m:
        if L < result:
            result = L
    else:
        for i in range(n):
            DFS(L + 1, s + coin[i])

if __name__ == "__main__":
    n = int(input())
    coin = sorted(list(map(int, input().split())), reverse=True)
    m = int(input())
    result = float('inf')
    DFS(0, 0)
    print(result)