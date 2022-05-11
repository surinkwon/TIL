'''
구현
리스트로 풀면 오히려 시간 초과. pop도 있고 그래서 그런듯
이차원 배열 계속 탐색하게 풀어도 몇 백 만번밖에 안 돼서 배열로 푸는 게 더 효율적
근데 배열도 pypy로 돌려야되고 python으로 돌리면 시간초과... 
'''

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

R, C, T = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(R)]
top_air_cleaner = 0
for i in range(R):
    if top_air_cleaner and room[i][0] == -1:
        bottom_air_cleaner = [i]
    elif room[i][0] == -1:
        top_air_cleaner = [i]

for i in range(R):
    for j in range(C):
        if room[i][j] != -1:
            room[i][j] = [room[i][j], room[i][j] // 5]

# 배열로 푼 방법
# micro_dust = []
# for i in range(R):
#     for j in range(C):
#         if room[i][j] == -1:
#             if top_air_cleaner:
#                 bottom_air_cleaner = (i, j)
#             else:
#                 top_air_cleaner = (i, j)
#         elif room[i][j]:
#             micro_dust.append([i, j, room[i][j]])


# for _ in range(T):
#     # 먼지 확산시키기
#     for i in range(len(micro_dust)):
#         r, c = micro_dust[i][0], micro_dust[i][1]
#         dust_amount = micro_dust[i][2]
#         spread_amount = dust_amount // 5
#         cnt = 0

#         if spread_amount > 0:
#             for d in range(4):
#                 nr = r + dr[d]
#                 nc = c + dc[d]
#                 if 0 <= nr < R and 0 <= nc < C:
#                     if nr == top_air_cleaner[0] and nc == top_air_cleaner[1]:
#                         continue
#                     elif nr == bottom_air_cleaner[0] and nc == bottom_air_cleaner[1]:
#                         continue
#                     else:
#                         cnt += 1
#                         micro_dust.append([nr, nc, spread_amount])
            
#             micro_dust[i][2] -= spread_amount * cnt
    
#     micro_dust.sort()
#     # 확산된 먼지 합치기
#     for i in range(len(micro_dust) - 1, 0, -1):
#         if micro_dust[i][0] == micro_dust[i-1][0] and micro_dust[i][1] == micro_dust[i-1][1]:
#             micro_dust[i-1][2] += micro_dust[i][2]
#             micro_dust.pop(i)
    
#     # 진공청소기 작동
#     for i in range(len(micro_dust) - 1, -1, -1):
#         if micro_dust[i][0] == 0 or micro_dust[i][0] == R - 1:
#             if micro_dust[i][1] != 0:
#                 micro_dust[i][1] -= 1
#             else:
#                 if micro_dust[i][0] == 0:
#                     micro_dust[i][0] += 1
#                 else:
#                     micro_dust[i][0] -= 1

#         elif micro_dust[i][0] == top_air_cleaner[0] or micro_dust[i][0] == bottom_air_cleaner[0]:
#             if micro_dust[i][1] != C - 1:
#                 micro_dust[i][1] += 1
#             else:
#                 if micro_dust[i][0] == top_air_cleaner[0]:
#                     micro_dust[i][0] -= 1
#                 else:
#                     micro_dust[i][0] += 1

#         elif micro_dust[i][1] == C - 1:
#             if micro_dust[i][0] >= bottom_air_cleaner[0]:
#                 if micro_dust[i][0] != R - 1:
#                     micro_dust[i][0] += 1
#                 else:
#                     micro_dust[i][1] -= 1
#             elif micro_dust[i][0] <= top_air_cleaner[0]:
#                 if micro_dust[i][0] != 0:
#                     micro_dust[i][0] -= 1
#                 else:
#                     micro_dust[i][1] -= 1

#         elif micro_dust[i][1] == 0:
#             if micro_dust[i][0] < top_air_cleaner[0] - 1:
#                 micro_dust[i][0] += 1
#             elif micro_dust[i][0] > bottom_air_cleaner[0] + 1:
#                 micro_dust[i][0] -= 1
#             else:
#                 micro_dust.pop(i)

# total_dust = 0
# for i in range(len(micro_dust)):
#     total_dust += micro_dust[i][2]

# print(total_dust)

for _ in range(T):
    # 먼지 확산
    for i in range(R):
        for j in range(C):
            if room[i][j] != -1 and room[i][j][0]:
                cnt = 0
                spread_amount = room[i][j][1]
                if spread_amount:
                    for d in range(4):
                        nr, nc = i + dr[d], j + dc[d]
                        if 0 <= nr < R and 0 <= nc < C and room[nr][nc] != -1:
                            room[nr][nc][0] += spread_amount
                            cnt += 1
                    room[i][j][0] -= spread_amount * cnt

    for r in range(top_air_cleaner[0] - 2, -1, -1):
            room[r + 1][0][0] = room[r][0][0]
            room[r + 1][0][1] = room[r][0][1]
    
    for r in range(bottom_air_cleaner[0] + 1, R - 1):
        room[r][0][0] = room[r + 1][0][0]
        room[r][0][1] = room[r + 1][0][1]

    for c in range(C - 1):
        room[0][c][0] = room[0][c + 1][0]
        room[0][c][1] = room[0][c + 1][1]
        room[R - 1][c][0] = room[R - 1][c + 1][0]
        room[R - 1][c][1] = room[R - 1][c + 1][1]
    
    for r in range(top_air_cleaner[0]):
            room[r][C - 1][0] = room[r + 1][C - 1][0]
            room[r][C - 1][1] = room[r + 1][C - 1][1]

    for r in range(R - 1, bottom_air_cleaner[0], -1):
        room[r][C - 1][0] = room[r - 1][C - 1][0]
        room[r][C - 1][1] = room[r - 1][C - 1][1]

    for c in range(C - 1, 1, -1):
        room[top_air_cleaner[0]][c][0] = room[top_air_cleaner[0]][c - 1][0]
        room[top_air_cleaner[0]][c][1] = room[top_air_cleaner[0]][c - 1][1]
        room[bottom_air_cleaner[0]][c][0] = room[bottom_air_cleaner[0]][c - 1][0]
        room[bottom_air_cleaner[0]][c][1] = room[bottom_air_cleaner[0]][c - 1][1]

    room[top_air_cleaner[0]][1] = [0, 0]
    room[bottom_air_cleaner[0]][1] = [0, 0]

    for i in range(R):
        for j in range(C):
            if room[i][j] != -1 and room[i][j][0]:
                room[i][j][1] = room[i][j][0] // 5


total_dust = 0
for i in range(R):
    for j in range(C):
        if room[i][j] != -1 and room[i][j][0]:
            total_dust += room[i][j][0]

print(total_dust)

