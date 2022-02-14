# 사람 수, 최대 공 받는 횟수, 공 넘겨주는 간격
N, M, L = map(int, input().split())
# 공 받은 횟수 리스트, 최종 공 넘긴 횟수, 공 받은 사람
ball_num = [0] * N
total = 0
ball_num[0] = 1
index = 0
# 공 받은 횟수가 홀수면
while True:
    if M in ball_num:
        break
    
    if ball_num[index] % 2:
        index += L
        if index >= N:
            index %= N 
        ball_num[index] += 1
# 공 받은 횟수가 짝수
    else:
        index -= L
        if index < 0:
            index += N
        ball_num[index] += 1
    total += 1


print(total)