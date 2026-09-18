data = input()
move = [
    (-2, -1), (-2, 1), (-1, 2), (1, 2),
    (2, 1), (2, -1), (-1, -2), (1, -2)]

row = int(data[1])
column = int(ord(data[0])) - int(ord('a')) + 1

count = 0

for i in move:
    next_row = row + i[1]
    next_column = column + i[0]

    if 1 <= next_row <= 8 and 1 <= next_column <= 8:
        count += 1

print(count)