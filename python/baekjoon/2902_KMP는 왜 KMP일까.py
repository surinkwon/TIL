# 이름 입력
memo = input()

# 맨 첫번째 문자를 출력 문자열에 저장
short = memo[0]

# 하이픈 뒤에 나오는 문자를 출력문자열에 저장
for i in range(1, len(memo)):
    if memo[i-1] == '-':
        short += memo[i]

print(short)