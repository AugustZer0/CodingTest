def check_sudoku():
    for i in range(9):
        row = set()
        col = set()
        for j in range(9):
            row.add(sudoku[i][j])
            col.add(sudoku[j][i])
        if len(row) != 9 and len(col) != 9:
            return False

    for x in range(0, 9, 3):
        for y in range(0, 9, 3):
            box = set()
            for a in range(3):
                for b in range(3):
                    box.add(sudoku[x+a][y+b])
            if len(box) != 9:
                return False
    return True

sudoku = [list(map(int, input().split())) for _ in range(9)]

if check_sudoku():
    print("YES")
else:
    print("NO")