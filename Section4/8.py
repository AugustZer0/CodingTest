n = int(input())
a = [list(map(int, input().split())) for _ in range (n)]
m = int(input())


# 회전
for i in range(m):
    x, y, z = map(int, input().split())
    # 인덱스로 인해서 +1 처리
    x -= 1
    
    # 좌로 이동
    if y == 0:
        a[x] = a[x][z:] + a[x][:z]
    
    # 우로 이동
    else:
        a[x] = a[x][-z:] + a[x][:-z]

# 모래시계 더하기
result = start = 0
end = n

for i in range(n):
    result += sum(a[i][start:end])
    
    if i < n // 2:
        start += 1
        end -= 1
    else:
        start -= 1
        end += 1

print(result)