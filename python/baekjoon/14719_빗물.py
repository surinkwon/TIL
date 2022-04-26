'''
창고 다각형과 비슷
높이가 같은 블록이 1칸 이상 떨어져있으면 그 사이에는 무조건 물이 고이게 됨
0을 제외한 모든 높이에서 물이 고이는 곳이 있는지 검사하고 더해주면 됨
'''
H, W = map(int, input().split())
heights = list(map(int, input().split()))
total = 0

for h in range(H, 0, -1):
    block_x = -1                                # 현재 높이의 블록이 이전에 있었는지 체크
    for x in range(W):
        if heights[x] >= h:                     # 블록의 높이가 현재 높이와 같거나 높다면
            if block_x == -1:                   # 이전에 현재 높이 블록이 없었으면 
                block_x = x                     # 지금 장소를 저장
            else:                               # 있었으면
                if x - block_x > 1:             # 두 블록 사이에 물이 고일 수 있으면
                    total += x - block_x - 1    # 물 고인 양 +
                    block_x = x                 # 현재 블록 장소 저장
                else:
                    block_x = x

print(total)
