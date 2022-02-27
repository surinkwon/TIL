N, M = map(int, input().split())
boxes = list(map(int, input().split()))
books = list(map(int, input().split()))
rest_total = 0

i = j = 0
# 책을 다 넣을 때까지
while j < M:
    # 박스 크기가 책 크기보다 크면 해당 박스 크기를 조정 후 다음 책으로 넘어감
    if boxes[i] > books[j]:
        boxes[i] -= books[j]
        j += 1
    # 박스 크기와 책 크기가 같으면 해당 박스 크기 조정 후 박스와 책 모두 다음으로 넘어감
    elif boxes[i] == books[j]:
        boxes[i] -= books[j]
        i += 1
        j += 1
    # 박스 크기가 책 크기보다 작으면 박스만 다음으로 넘어감
    else:
        i += 1

# 박스에서 남은 공간 모두 더함
for i in range(N):
    rest_total += boxes[i]


print(rest_total)

