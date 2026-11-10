t = int(input())

for test_case in range(1, t + 1):
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    result = []

    for x in range(n - m + 1):
        for y in range(n - m + 1):
            tmp = 0
            for a in range(m):
                for b in range(m):
                    tmp += arr[x + a][y + b]
            result.append(tmp)

    print(f"#{test_case} {max(result)}")

