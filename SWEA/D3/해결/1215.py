for test_case in range(1, 11):
    n = int(input())
    arr = [list(input()) for _ in range(8)]
    cnt = 0

    for i in range(len(arr)):
        for j in range(len(arr) - n + 1):
            lines = arr[i][j: j + n]
            if lines == lines[::-1]:
                cnt += 1

    for i in range(len(arr)):
        for j in range(len(arr) - n + 1):
            lines = [arr[j + k][i] for k in range(n)]
            if lines == lines[::-1]:
                cnt += 1

    print(f"#{test_case} {cnt}")