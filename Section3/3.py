from itertools import combinations

n, k = map(int, input().split())

a = list(map(int, input().split()))
l = []

for comb in combinations(a, 3):
    l.append(sum(comb))

l = list(set(l))
l.sort(reverse=True)

print(l[k - 1])
            