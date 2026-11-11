for test_case in range(1, 11):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    result = 0

    for i in range(len(arr)):
        a = 0
        b = 0
        for j in range(len(arr)):
            a += arr[i][j]
            b += arr[j][i]

        result = max(result, a, b)


    cross_sum = 0
    reverse_cross_sum = 0
    for i in range(len(arr)):
        cross_sum += arr[i][i]
        reverse_cross_sum += arr[-i - 1][i]

    result = max(result, cross_sum, reverse_cross_sum)
    print(f"#{test_case} {result}")


