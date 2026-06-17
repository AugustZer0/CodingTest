board = [list(map(int, input().split()))for _ in range(9)]


def check(a):
    # 행(가로)과 열(세로) 검사
    for i in range(9):
        row_check = [0] * 10
        col_check = [0] * 10
        
        for j in range(9):
            row_num = board[i][j]
            if row_check[row_num] == 1:
                return "NO"
            row_check[row_num] = 1
        
        
            col_num = board[j][i]
            if col_check[col_num] == 1:
                return "NO"
            col_check[col_num] = 1
    
    # 3 x 3 검사(i, j는 꼭짓점 좌표)
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            box_check = [0] * 10
            for x in range(3):
                for y in range(3):
                    num = board[i + x][j + y]
                    if box_check[num] == 1:
                        return "NO"
                    box_check[num] = 1
    return "YES"

print(check(board))