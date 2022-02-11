# 성 크기
length, width = map(int, input().split())
# 이차원 배열로 경비병 정보 받음
castle = []
for floor in range(length):
    castle.append(list(input()))

# 경비병에 대한 열정보를 받기 위한 리스트, 행, 열별로 필요한 경비병 수
gards = [0] * width
r_need = c_need = 0

for f in castle:
    # 경비병이 해당 층에 있으면
    if 'X' in f:
        # 해당 열에 경비병이 있으면 경비병 정보 리스트에 1
        for gard in range(width):
            if f[gard] == 'X':
                gards[gard] += 1

    # 없으면 행에 필요한 경비병 수 + 1
    else:
        r_need += 1

# 경비병 정보 리스트를 돌며 없는 열 수만큼 열에 필요한 경비병 수 + 1
for person in gards:
    if person:
        continue
    c_need += 1

# 둘 중 더 큰 값이 필요한 경비병 수 
if c_need <= r_need:
    print(r_need)
else:
    print(c_need)

