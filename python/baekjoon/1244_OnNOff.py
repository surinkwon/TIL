# 스위치 켜고 끄기

# 스위치 상태, 학생 정보를 받음
switch_num = int(input())
first_switch = list(map(int, input().split()))
student_num = int(input())
student_lst = []

# 학생별 정보를 리스트 형태로 학생 리스트에 저장
for _ in range(student_num):
    student_lst.append(list(map(int, input().split()))) 

# 학생 성별에 따라 스위치 상태 조작
for student in student_lst:
    
    # 남학생일 때
    if student[0] == 1:

        # 받은 번호의 배수를 판별하여 스위치 조작
        for index in range(switch_num):
            if (index + 1) % student[1] == 0:
                if first_switch[index] == 0:
                    first_switch[index] = 1
                else:
                    first_switch[index] = 0
    
    # 여학생일 때
    else:
        i = 1 # 빋은 스위치 번호를 기준으로 더하고 빼줄 수

        # 인덱스가 넘어가는 범위는 더하거나 빼줄 수 없기 때문에 i 값을 제한
        if student[1] <= student_num // 2:
            c_i = student[1]
        else:
            c_i = switch_num + 1 - student[1]
        
        # 양쪽의 스위치 상태가 같으면 다음 스위치 판별
        while i < c_i:
            if first_switch[student[1] - 1 - i] == first_switch[student[1] - 1 + i]:
                i += 1
            else:
                break
        
        # 같은 상태의 스위치가 없다면 받은 번호의 스위치 상태만 바꿈
        if i == 1:
            if first_switch[student[1] - 1] == 0:
                first_switch[student[1] - 1] = 1
            else:
                first_switch[student[1] - 1] = 0
        
        # 같은 스위치 상태가 있다면 모두 바꿈
        else:
            for j in range(student[1] - i, student[1] - 1 + i):
                if first_switch[j] == 1:
                    first_switch[j] = 0
                else:
                    first_switch[j] = 1
                
# 한 줄에 20개씩 스위치 상태 출력
rlt = ''
for idx in range(switch_num):
    if (idx + 1) % 20 == 0:
        rlt += str(first_switch[idx]) + '\n'
    else:
        rlt += str(first_switch[idx]) + ' '
print(rlt[:(switch_num * 2) - 1])

