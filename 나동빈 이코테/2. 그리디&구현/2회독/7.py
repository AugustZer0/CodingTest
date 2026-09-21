data = input()

column = int(ord(data[0])) - int(ord('a')) + 1
row = int(data[1])

move = [
    (-2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (-1, -2), (1, -2)
]

count = 0

for i in move:
    next_column = column + i[0]
    next_row = row + i[1]

    if 1 <= next_column <= 8 and 1 <= next_row <= 8:
        count += 1

print(count)