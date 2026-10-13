from itertools import combinations

n, k = map(int, input().split())
arr = list(map(int, input().split()))
tmp = []

for comb in combinations(arr, 3):
    tmp.append(sum(comb))

tmp = sorted(list(set(tmp)), reverse=True)

print(tmp[k-1])

"""
sorted (내장 함수)
sorted(a), 세트, 리스트, 튜플, 문자열 가능함

sort (메서드) 
반드시 리스트 뒤에 객체 점을 붙여서 호출해야함(리스트만 가능)
a.sort()
"""