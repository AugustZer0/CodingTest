"""
간단한 정렬 합치지 말고 투포인터 문제임
"""

n = int(input())
n_arr = list(map(int, input().split()))
m = int(input())
m_arr = list(map(int, input().split()))

p1 = p2 = 0
result = []

while p1 < n and p2 < m:
    if n_arr[p1] <= m_arr[p2]:
        result.append(n_arr[p1])
        p1 += 1
    else:
        result.append(m_arr[p2])
        p2 += 1

if p1 < n:
    result.extend(n_arr[p1:])
if p2 < m:
    result.extend(m_arr[p2:])

print(*result)