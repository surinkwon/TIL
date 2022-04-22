'''
그대로 구현
문제를 잘 읽자. 나누어진다는 게 나눠지고 이동도 한다는 게 아니라 그냥 그 자리에서 나눠진다는 거다.
방향값을 다 더해서 짝수인게 각 방향값들이 모두 홀수거나 모두 짝수임을 보장하지는 않는다.
'''
dr = [-1, -1, 0, 1, 1, 1, 0, -1]
dc = [0, 1, 1, 1, 0, -1, -1, -1]


N, M, K = map(int, input().split())
fireballs = []
for i in range(M):
    # 정보: 행, 열, 질량, 속력, 방향
    fireballs.append(list(map(int, input().split())))
    fireballs[i][4] = [fireballs[i][4]]                 # 나중에 방향이 여러개 있는지를 따질 거라서 리스트로 만들어줌 
    fireballs[i][0] = (fireballs[i][0] - 1) % N         # 좌표가 1부터 시작하므로 0부터 좌표를 쓰기 위해 한 칸씩 줄여줌
    fireballs[i][1] = (fireballs[i][1] - 1) % N

# K번 명령
for _ in range(K):
    # 모든 파이어볼이 정해진 방향으로 정해진 속력만큼 이동
    for i in range(len(fireballs)):
        r, c, m, s, d = fireballs[i][0], fireballs[i][1], fireballs[i][2], fireballs[i][3], fireballs[i][4][0]
        nr, nc = (r + dr[d] * s + N) % N, (c + dc[d] * s + N) % N
        fireballs[i] = [nr, nc, m, s, [d]]
        
    fireballs.sort(key=lambda x:(x[0], x[1]))

    # 파이어볼이 한 자리에 여러 개가 있으면 합침
    cnt = 1
    for idx in range(len(fireballs) - 1, -1, -1):
        if idx > 0 and fireballs[idx][0] == fireballs[idx-1][0] and fireballs[idx][1] == fireballs[idx-1][1]:
            fireballs[idx-1][2] += fireballs[idx][2]
            fireballs[idx-1][3] += fireballs[idx][3]
            fireballs[idx-1][4] += fireballs[idx][4]
            cnt += 1
            # 합쳐진 파이어볼에 대한 정보는 삭제
            fireballs.pop(idx)
        else:
            if cnt > 1:
                r, c, m, s = fireballs[idx][0], fireballs[idx][1], fireballs[idx][2], fireballs[idx][3]
                m //= 5

                # 합쳐진 파이어볼이 나눠질 때 질량이 0이 되면 삭제
                if m == 0:
                    fireballs.pop(idx)
                    cnt = 1
                    continue
                s //= cnt

                # 여러 파이어볼의 방향이 모두 짝수 혹은 홀수인지 아닌지를 확인
                d = fireballs[idx][4][0] % 2
                for direction in range(1, len(fireballs[idx][4])):
                    # 하나라도 다른 게 있으면 홀수 방향으로 쪼개짐
                    if fireballs[idx][4][direction] % 2 != d:
                        fireballs[idx][4] = [1, 3, 5, 7]
                        break
                
                # 홀수방향으로 쪼개지는 게 아니면 짝수방향으로 쪼개짐
                if fireballs[idx][4] != [1, 3, 5, 7]: fireballs[idx][4] = [0, 2, 4, 6]
                
                # 좌표는 그대로 하고 방향만 다르게 쪼개서 다시 파이어볼 정보에 추가
                for d in range(3):
                    d = fireballs[idx][4][d]
                    fireballs.append([r, c, m, s, [d]])
                d = fireballs[idx][4][3]
                fireballs[idx] = [r, c, m, s, [d]]
                cnt = 1

total_mess = 0
for i in range(len(fireballs)):
    total_mess += fireballs[i][2]

print(total_mess)




