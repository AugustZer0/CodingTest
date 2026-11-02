if __name__ == "__main__":
    n, m = map(int, input().split())
    arr = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(m):
        s, e, v = map(int, input().split())
        arr[s - 1][e - 1] = v

    for x in arr:
        print(*x)