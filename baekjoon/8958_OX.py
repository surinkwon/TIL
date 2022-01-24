# 테스트 케이스 개수 및 퀴즈 결과 입력
test_num = int(input())

# 연속된 점수를 담을 변수
seq_o = 0
score = 0

for _ in range(test_num):
    quiz_rlt = input()

    seq_o = 0
    score = 0

    for o in quiz_rlt:
        if o == 'O':
            seq_o += 1
            score += seq_o
        else:
            seq_o = 0
    
    print(score)

