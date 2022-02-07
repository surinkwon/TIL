# 네 번째 점
a = tuple(map(int, input().split()))
b = tuple(map(int, input().split()))
c = tuple(map(int, input().split()))

x = [a[0], b[0], c[0]]
y = [a[1], b[1], c[1]]

x.sort()
y.sort()

if x[0] == x[1]:
    x_d = x[2]
else:
    x_d = x[0]

if y[0] == y[1]:
    y_d = y[2]
else:
    y_d = y[0]

print(f'{x_d} {y_d}')