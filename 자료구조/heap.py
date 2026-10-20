"""
힙이란?
가장 작은 값(또는 가장 큰 값)을 빠르게 꺼내기 위한 트리 모양 자료구조
전체를 정렬해 두지 않고, 루트에 최소값(최대값)만 오도록 느슨하게 정리해 두는게 핵심

최소힙: 부모 ≤ 자식
최대힙: 부모 ≥ 자식

형제 끼리는 순서 X
"""

import heapq

arr = list(map(int, input().split()))


# 최소힙
min_heap = []

# 힙 배열 삽입
for x in arr:
    heapq.heappush(min_heap, x)

print(heapq.heappop(min_heap))
print(min_heap[0])

# 최대힙: 값에 -를 붙여서 넣고, 꺼낼 때 다시 - 붙이기
max_heap = []

for x in arr:
    heapq.heappush(max_heap, -x)

print(-heapq.heappop(max_heap))
