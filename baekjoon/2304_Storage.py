from sys import stdin

num = int(input())
storage_lst = []

for _ in range(num):
    storage_lst.append(list(map(int, stdin.readline().split())))

# 창고 리스트를 x좌표 기준으로 정렬하고 각 좌표 리스트에 좌표 저장
x = []
y = []
storage_lst.sort()
for po in storage_lst:
    x.append(po[0])
    y.append(po[1])

total = 0
area = 0
max_height_id = y.index(max(y))
max_cnt = y.count(max(y))

# 다각형의 개수가 여러개일 때
if num != 1:
    # x좌표가 가장 높은 다각형의 x좌표보다 작을 때
    for x_loc in range(x[0], x[max_height_id]):
        if x_loc in x: # 다각형의 높이를 더하고 다음 다각형의 높이가 더 크면 더할 높이를 교체
            if area < y[x.index(x_loc)]:
                area = y[x.index(x_loc)]
        total += area
    area = 0

    # 마지막 다각형부터 가장 높은 다각형 전까지
    for x_loc in range(x[-1], x[max_height_id + max_cnt - 1], -1):
        if x_loc in x: 
            if area < y[x.index(x_loc)]:
                area = y[x.index(x_loc)]
        total += area
    
    # 가장 높은 다각형이 차지하는 x좌표만큼 높이를 더해줌
    for x_loc in range(x[max_height_id], x[max_height_id + max_cnt - 1] + 1):
        total += max(y)

    print(total)

else:
    print(storage_lst[0][1])

