N = int(input())

scores = []
total_dec_num = 0

for _ in range(N):
    scores.append(int(input()))

for i in range(N - 2, -1, -1):
    if scores[i] >= scores[i + 1]:
        total_dec_num += scores[i] - scores[i + 1] + 1
        scores[i] = scores[i + 1] - 1

print(total_dec_num)