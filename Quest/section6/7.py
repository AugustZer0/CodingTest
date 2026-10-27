def DFS(L, s):
    global res
    # 최솟값 기준 가지치기
    if L > res:
        return

    # 목표 금액 초과 방지
    if s > m:
        return

    if s == m:
        if L < res:
            res = L
    else:
        for i in range(n):
            DFS(L + 1, s + coin[i])


if __name__ == "__main__":
    n = int(input())
    coin = sorted(map(int, input().split()), reverse=True)
    m = int(input())
    res = float('inf')
    DFS(0, 0)
    print(res)