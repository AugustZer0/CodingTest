def DFS(L, s):
    global res

    if s > m:
        return

    if L >= res:
        return

    if s == m:
        if L < res:
            res = L

    else:
        for i in coins:
            DFS(L + 1, s + i)

if __name__ == "__main__":
    n = int(input())
    coins = sorted(map(int, input().split()), reverse=True)
    m = int(input())
    res = float('inf')
    DFS(0, 0)
    print(res)