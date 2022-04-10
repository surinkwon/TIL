'''
에라토스테네스의 체
'''

N, M = map(int, input().split())
d = [0] * (M + 1)

# 2부터 소수를 찾고 그 소수의 배수는 모두 지워버림
for i in range(2, M + 1):
    if d[i] == 0:
        for j in range(i, M + 1, i):
            if i != j:
                d[j] = 1

# 1은 소수로 치지 않음
d[1] = 1

# 소수만 출력
for i in range(N, M + 1):
    if d[i] == 0:
        print(i)
