"""
파이썬의 경우 반올림을 구하려면 위와 같은 방식을 이용해야 함.
round를 사용하면 사사오입으로 가지 않고 짝수 반올림을 사용하기 때문
"""

n = int(input())
arr = list(map(int, input().split()))

avg = int(sum(arr) / n + 0.5)
min_value = float('inf')

score = 0
result = 0

for idx, value in enumerate(arr):
    tmp = abs(value - avg)
    if tmp < min_value:
        min_value = tmp
        score = value
        result = idx + 1
    elif tmp == min_value:
        if value > score:
            score = value
            result = idx + 1

print(avg, result)