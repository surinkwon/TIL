# 학점계산
score = input()
scores = ['A', 'B', 'C', 'D', 'F']
avs = [4.0, 3.0, 2.0, 1.0, 0.0]

for i in range(5):
    if score[0] == scores[i]:
        av = avs[i]

if score.find('+') > 0:
    av += 0.3
elif score.find('-') > 0:
    av -= 0.3

print(av)
