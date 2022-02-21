# 문자가 같은 자판에 있는지 확인하기 위한 dat
phone = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
Q, W = map(int, input().split()) # 문자 하나를 치는 데 드는 시간, 같은 자판에 있을 때 기다리는 시간
m = input()
total = 0

# 문자가 이전 문자와 같은 자판에 있었는지를 확인하기 위해 num 변수 정의
# 첫번째 num은 맨 처음 문자의 자판 번호로 저장
for i in range(len(phone)):
    if m[0] in phone[i]:
        num = i

for letter in m:
    if letter != ' ':
        for phone_num in range(len(phone)):
            if letter in phone[phone_num]:
                # 이전 문자와 자판 번호가 같지 않으면 해당 문자를 치는 데 걸리는 시간만 더함
                if phone_num != num: 
                    total += (phone[phone_num].index(letter) + 1) * Q
                # 이전 문자와 자판 번호가 같으면 W도 더해줌
                else:
                    total += W + (phone[phone_num].index(letter) + 1) * Q
                num = phone_num # 자판 번호를 현재 자판번호로 갱신
                break
    else:
        total += Q
        # 공백문자가 있는 경우 앞뒤 문자의 자판 번호가 같더라도 W만큼 기다리지 않아도 되기 때문에
        # 인덱스 범위를 넘어가는 값으로 초기화해줌
        num = len(phone) 

# 자판 번호를 맨 처음 문자가 속한 번호로 저장한 후 문자열을 검사했기 때문에
# W가 한 번 더 더해져 이를 빼줌
print(total - W)