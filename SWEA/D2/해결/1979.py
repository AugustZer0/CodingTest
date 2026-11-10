t = int(input())

for test_case in range(1, t + 1):
    n, k = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    cnt = 0

    for i in range(n):
        col_arr = []
        row_arr = []
        col_tmp = 0
        row_tmp = 0
        for j in range(n):
            col_arr.append(arr[i][j])
            row_arr.append(arr[j][i])

        for col in col_arr:
            if col == 1:
                col_tmp += 1
            else:
                if col_tmp == k:
                    cnt += 1
                col_tmp = 0
        if col_tmp == k:
            cnt += 1

        for row in row_arr:
            if row == 1:
                row_tmp += 1
            else:
                if row_tmp == k:
                    cnt += 1
                row_tmp = 0
        if row_tmp == k:
            cnt += 1

    print(f"#{test_case} {cnt}")
