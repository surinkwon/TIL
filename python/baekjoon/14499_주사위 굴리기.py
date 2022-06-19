'''
구현
문제를 잘 읽자... 여기에선 x가 r이고 y가 c다 
문제 조건에서 x <= N-1, y <= M-1이라고 명시됨...
'''
# 1-6, 3-4, 2-5
# 북이나 남으로 이동하면 무조건 동, 서는 같은 숫자
# 동이나 서로 이동하면 무조건 북, 남은 같은 숫자
# 북으로 이동하면 남이 원래 바닥 숫자, 북은 그 반대로 짝지어진 숫자
# 남으로 이동하면 북이 원래 바닥 숫자
# 동으로 이동하면 서가 원래 바닥 숫자
# 서로 이동하면 동이 원래 바닥 숫자
# 동: 1, 서: 2, 북: 3, 남: 4
import sys

dr = [0, 0, 0, -1, 1]
dc = [0, 1, -1, 0, 0]

dice_num = [0] * 7
point = [6, 3, 4, 2, 5]
opp = {1: 6, 2: 5, 3: 4, 4: 3, 5: 2, 6: 1}

N, M, x, y, K = map(int, input().split())
dice_map = [list(map(int, input().split())) for _ in range(N)]

order = list(map(int, sys.stdin.readline().split()))

for i in range(K):
    d = order[i]
    nx, ny = x + dr[d], y + dc[d]
    if 0 <= nx < N and 0 <= ny < M:
        # point 조정
        n_floor = point[d]
        if d % 2:
            point[d+1] = point[0]
            point[d] = opp[point[0]]
            point[0] = n_floor
        else:
            point[d-1] = point[0]
            point[d] = opp[point[0]]
            point[0] = n_floor
        
        bp = 1
        # 현재 바닥 숫자 조정
        if dice_map[nx][ny]:
            dice_num[n_floor] = dice_map[nx][ny]
            dice_map[nx][ny] = 0
        else:
            dice_map[nx][ny] = dice_num[n_floor]
        
        print(dice_num[opp[n_floor]])
        x, y = nx, ny

