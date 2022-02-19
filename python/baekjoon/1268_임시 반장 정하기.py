# 학생 수 
n = int(input())

# 표
number_grade = [list(input().split()) for _ in range(n)]
# 표를 행잉 학년인 이차원 배열로 변경
grade_number = [[0] * n for _ in range(5)]

for i in range(5):
    for j in range(n):
        grade_number[i][j] = number_grade[j][i]

# 각 학생들의 같은 반 정보를 담을 리스트
cnt = [[0] * n for _ in range(n)]

# 같은 반을 한 횟수를 세서 같은 반 정보 리스트에 저장
for i in range(5):
    for j in range(n):
        for k in range(n):
            if grade_number[i][j] == grade_number[i][k]:
                if j != k and cnt[j][k] == 0:
                    cnt[j][k] += 1

cnt_s = [0] * n
for i in range(n):
    for j in range(n):
        if cnt[i][j]:
            cnt_s[i] += 1

print(cnt_s.index(max(cnt_s)) + 1)

