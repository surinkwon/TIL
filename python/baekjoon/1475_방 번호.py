room_num = input()

numbers = [0] * 10

# 번호를 인덱스로 하는 리스트를 만들고 방 번호에 든 숫자 개수 저장
for i in range(len(room_num)):
    numbers[int(room_num[i])] += 1

# 6, 9가 아닌 숫자들 중 최댓값과 6, 9의 값을 저장할 변수
max_num = 0
sn = 0


for i in range(len(numbers)):
    if i != 6 and i != 9:
        if max_num < numbers[i]:
            max_num = numbers[i]
    else:
        sn += numbers[i]

# 6, 9는 서로 대체될 수 있으므로 그 경우를 계산해줌
if sn % 2:
    sn = sn // 2 + 1
else:
    sn //= 2

rlt = max(sn, max_num)

print(rlt)
