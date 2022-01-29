# 전자레인지
T = int(input())
a_s = [300, 0]
b_s = [60, 0]
c_s = [10, 0]

if T >= a_s[0]:
    a_s[1] += (T // a_s[0])
    T -= (T // a_s[0]) * a_s[0]
if T >= b_s[0]:
    b_s[1] += (T // b_s[0])
    T -= (T // b_s[0]) * b_s[0]
if T >= c_s[0]:
    c_s[1] += (T // c_s[0])
    T -= (T // c_s[0]) * c_s[0]

if T:
    print(-1)
else:
    print(f'{a_s[1]} {b_s[1]} {c_s[1]}')