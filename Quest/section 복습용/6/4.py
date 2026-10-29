import sys

def DFS(L, s):
    if s > total:
        return
    if L == n:
        if s == total // 2:
            print("YES")
            sys.exit(0)
    else:
        DFS(L + 1, s + arr[L])
        DFS(L + 1, s)

if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    total = sum(arr)
    if total % 2 == 1:
        print("NO")
    else:
        DFS(0, 0)
        print("NO")