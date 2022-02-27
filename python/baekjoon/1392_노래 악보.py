N, Q = map(int, input().split())
scores = [0] * (N + 1)
questions = [0] * Q

# 악보 인덱스를 나중에 사용하기 위해 맞춰줌
for i in range(1, N + 1):
    scores[i] = int(input())

for i in range(Q):
    questions[i] = int(input())

# 총 시간 구하기
total_time = 0
for idx in range(len(scores)):
    total_time += scores[idx]

# 시간을 인덱스로 하는 리스트
times = [0] * (total_time + 1)

# 해당 시간에 어떤 악보가 연주되고 있는지 저장
score_times = 0
time = 0
for score in range(1, len(scores)):
    score_times += scores[score]
    while time < score_times:
        times[time] = score
        time += 1

for i in range(len(questions)):
    print(times[questions[i]])

