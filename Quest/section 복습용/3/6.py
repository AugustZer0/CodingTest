n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]


cross_sum = 0
reverse_cross_sum = 0
result = 0

for i in range(n):
    col_sum = 0
    row_sum = 0
    for j in range(n):
        col_sum += arr[j][i]
        row_sum += arr[i][j]
    result = max(result, col_sum, row_sum)

for i in range(n):
    cross_sum += arr[i][i]
    reverse_cross_sum += arr[i][n - i - 1]

print(max(result, cross_sum, reverse_cross_sum))