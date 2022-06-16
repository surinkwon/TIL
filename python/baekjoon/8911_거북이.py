'''
구현
'''

dy = [-1, 0, 1, 0]
dx = [0, -1, 0, 1]

d = 0

N = int(input())

for _ in range(N):
    order = input()
    x, y = 0, 0

    place_lst = [(0, 0)]

    for i in range(len(order)):
        if order[i] == 'F':
            x, y = x + dx[d], y + dy[d]
            place_lst.append((x, y))
        elif order[i] == 'B':
            x, y = x - dx[d], y - dy[d]
            place_lst.append((x, y))
        elif order[i] == 'L':
            d = (d + 1) % 4
            place_lst.append((x, y))
        else:
            d = (d + 3) % 4
            place_lst.append((x, y))
    
    x_compare_lst = sorted(place_lst, key=lambda i: i[0])
    y_compare_lst = sorted(place_lst, key=lambda i: i[1])

    x_d = abs(x_compare_lst[0][0] - x_compare_lst[-1][0])
    y_d = abs(y_compare_lst[0][1] - y_compare_lst[-1][1])

    print(x_d * y_d)