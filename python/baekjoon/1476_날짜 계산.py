'''
E는 15로 나눈 나머지
S는 28로 나눈 나머지
M은 19로 나눈 나머지 년도로 표시됨
(각각이 0이면 해당 숫자로 표시됨)

이를 이용해서 풀이
'''
def rest(num1, num2):
    rlt = num1 % num2
    if rlt:
        return rlt
    else:
        return num2

E, S, M = map(int, input().split())

i = 1
while True:
    rest_e = rest(i, 15)
    rest_s = rest(i, 28)
    rest_m = rest(i, 19)

    if rest_e == E and rest_s == S and rest_m == M:
        break

    i += 1

print(i)
