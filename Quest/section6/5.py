def DFS(L, s, ts):
    global res
    # 현재 상태에서 앞으로 남은 원소를 전부 다 골라도 res 보다 낮으면 가지침
    if s + (total - ts) < res:
        return
    if s > c:
        return
    if L == n:
        if s > res:
            res = s
    else:
        DFS(L + 1, s + arr[L], ts + arr[L])
        DFS(L + 1, s, ts + arr[L])


if __name__ == "__main__":
    c, n = map(int, input().split())
    arr = [int(input()) for _ in range(n)]
    total = sum(arr)
    res = -float('inf')
    DFS(0, 0, 0)
    print(res)