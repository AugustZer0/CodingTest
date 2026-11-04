n = int(input())
n_arr = list(map(int, input().split()))
m = int(input())
m_arr = list(map(int, input().split()))

p1 = 0
p2 = 0
result = []

while n > p1 and m > p2:
    if n_arr[p1] >= m_arr[p2]:
        result.append(m_arr[p2])
        p2 += 1
    else:
        result.append(n_arr[p1])
        p1 += 1

if p1 != 0:
    result.extend(n_arr[p1:])

if p2 != 0:
    result.extend(m_arr[p2:])

print(*result)