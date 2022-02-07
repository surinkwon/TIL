# 테스트 케이스 수 저장
test_case_num = int(input())

for _ in range(test_case_num):
    score_list = list(map(int, input().split()))
    total = 0
    avg = 0
    over_avg_num = 0

    for score_index in range(1, len(score_list)):
        total += score_list[score_index]
    avg = total / score_list[0]

    for student in range(1, len(score_list)):
        if score_list[student] > avg:
            over_avg_num += 1
    
    over_avg_percent = over_avg_num / score_list[0] * 100

    print(f'{round(over_avg_percent, 3):.3f}%')

    