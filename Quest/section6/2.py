def DFS(v):
    if v > 7:
        return
    else:
        DFS(v * 2)
        print(v, end=' ')   # 위치에 따라 전위(앞) 중위(가운데) 후위(뒤)
        DFS(v * 2 + 1)
if __name__ == "__main__":
    DFS(1)