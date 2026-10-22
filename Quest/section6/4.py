import sys

def DFS(L, sum):
    if sum > total // 2:
        return
    if L == n:
        if sum == (total - sum):
            print("YES")
            sys.exit(0)
    else:
        DFS(L + 1, sum + arr[L])
        DFS(L + 1, sum)



if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    total = sum(arr)
    DFS(0, 0)
    print("NO")

"""
def DFS(L, s):
    if s > total // 2:
        return False
    if L == n:
        return s == total - s
    return DFS(L + 1, s + arr[L]) or DFS(L + 1, s) 


if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    total = sum(arr)
    print("YES" if DFS(0, 0) else "NO")
"""