def check_sudoku():
    # 가로, 세로에 대한 체크
    for i in range(9):
        col_set = set()
        row_set = set()
        for j in range(9):
            col_set.add(arr[i][j])
            row_set.add(arr[j][i])
        if len(col_set) != 9 or len(row_set) != 9:
            return False
    # 박스 단위 체크
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            box_set = set()
            for a in range(3):
                for b in range(3):
                    box_set.add(arr[i + a][j + b])
            if len(box_set) != 9:
                return False
    return True



arr = [list(map(int, input().split())) for _ in range(9)]

if check_sudoku():
    print("YES")
else:
    print("NO")