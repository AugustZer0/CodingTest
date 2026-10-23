import sys

def DFS(L, s):
    if s > total // 2:
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
        # 돌아왔을 때 종료가 안된다면 NO
        print("NO")
