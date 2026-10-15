n = int(input())
arr = list(map(int, input().split()))

res = [0] * n

for i in range(n):
    for j in range(n):
        if arr[i] == 0 and res[j] == 0:
            res[j] = i + 1
            break
        elif res[j] == 0:
            arr[i] -= 1

print(*res)