n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

largest = 0

for i in range(n):
    sum_row = 0
    sum_col = 0
    for j in range(n):
        sum_row += arr[j][i]
        sum_col += arr[i][j]
    largest = max(largest, sum_row, sum_col)

sum_cross = 0
sum_reverse_cross = 0
for a in range(n):
    sum_cross += arr[a][a]
    sum_reverse_cross += arr[a][n-1-a]

print(max(largest,sum_cross, sum_reverse_cross))