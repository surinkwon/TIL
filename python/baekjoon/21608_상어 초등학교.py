dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

N = int(input())

# 학생들의 선호 학생 정보, 자리 정하는 순서
students_like = [0] * (N ** 2 + 1)
order = []
classroom = [[0] * N for _ in range(N)]

# 입력 받은 정보를 선호학생 정보, 정하는 순서 배열에 저장
for i in range(N ** 2):
    student_like_data = list(map(int, input().split()))
    students_like[student_like_data[0]] = student_like_data[1:]
    order.append(student_like_data[0])

# 첫 학생은 항상 1, 1 자리에 배정됨
classroom[1][1] = order[0]

# 자리 배정
for student_num in range(1, len(order)):
    seat = (N, N, -1, -1)

    for r in range(N):
        for c in range(N):

            # 빈 자리일 때 비교
            if classroom[r][c] == 0:
                tmp_seat = [r, c, 0, 0]

                for d in range(4):
                    nr, nc = r + dr[d], c + dc[d]
                    if 0 <= nr < N and 0 <= nc < N:
                        if classroom[nr][nc] == 0 :
                            tmp_seat[2] += 1
                        elif classroom[nr][nc] in students_like[order[student_num]]:
                            tmp_seat[3] += 1
                
                # 자리 배정 조건에 따라 배정할지 결정 
                if seat[3] < tmp_seat[3]:
                    seat = tmp_seat
                elif seat[3] == tmp_seat[3] and seat[2] < tmp_seat[2]:
                    seat = tmp_seat
                elif seat[3] == tmp_seat[3] and seat[2] == tmp_seat[2] and seat[0] > r:
                    seat = tmp_seat
                elif seat[3] == tmp_seat[3] and seat[2] == tmp_seat[2] and seat[0] == r and seat[1] > c:
                    seat = tmp_seat
    
    classroom[seat[0]][seat[1]] = order[student_num]

# 만족도 계산
satisfaction = 0

for r in range(N):
    for c in range(N):
        like_num = 0
        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]
            if 0 <= nr < N and 0 <= nc < N and classroom[nr][nc] in students_like[classroom[r][c]]:
                like_num += 1
        
        if like_num:
            satisfaction += 10 ** (like_num - 1)

print(satisfaction)





