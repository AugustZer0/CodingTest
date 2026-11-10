def rotate(a):
    global n
    result = []
    for x in range(n):
        row = []
        for y in reversed(range(n)):
            row.append(a[y][x])
        result.append(row)
    return result

t = int(input())

for test_case in range(1, t + 1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]

    rotate_90 = rotate(arr)
    rotate_180 = rotate(rotate_90)
    rotate_270 = rotate(rotate_180)

    print(f"#{test_case}")
    for k in range(n):
        print(*rotate_90[k], sep='', end=' ')
        print(*rotate_180[k], sep='', end=' ')
        print(*rotate_270[k], sep='')