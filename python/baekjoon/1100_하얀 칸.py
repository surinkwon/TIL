chess = [0] * 8
total = 0

for row in range(len(chess)):
    chess[row] = input()

for row in range(len(chess)):
    if row % 2:
        for square in range(len(chess[row])):
            if square % 2 and chess[row][square] == 'F':
                total += 1
    else:
        for square in range(len(chess[row])):
            if square % 2 == 0 and chess[row][square] == 'F':
                total += 1

print(total)
