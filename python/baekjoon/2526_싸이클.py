# 인덱스 찾는 함수
def findIndex(lst, num):
    for i in range(len(lst)):
        if lst[i] == num:
            id = i
            break
    return id


N, P = map(int, input().split())
numbers = [N]
i = 0
# 연산으로 나오는 수가 중복되지 않을 때까지 numbers에 저장
while True:
    if (numbers[i] * N) % P not in numbers:
        numbers.append((numbers[i] * N) % P)
    # 중복되는 수가 나왔다면 그 수의 인덱스번호를 찾고 나옴
    else:
        idx = findIndex(numbers, (numbers[i] * N) % P)
        break
    i += 1

total = 0
# 해당 수부터 리스트 끝까지 길이를 재면 중복되는 수의 개수가 나옴
for _ in range(idx, len(numbers)):
    total += 1

print(total)