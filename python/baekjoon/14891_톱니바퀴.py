'''
N극은 0, S극은 1
여러 함수를 만들어서 풀어보았다.
turn 함수는 톱니바퀴리스트와 방향을 받아서 방향대로 톱니바퀴를 돌리는 함수
turnDirection함수는 왼쪽과 오른쪽 톱니바퀴를 받아서 톰니바퀴가 돌 방향을 구하는 함수
turnGears함수는 톱니바퀴 리스트와 방향 리스트를 받아서 방향대로 돌린 리스트를 반환하는 함수이다.
'''

# 톱니바퀴리스트와 방향을 받아서 방향대로 톱니바퀴를 돌리는 함수
def turn(lst, direction):
    if direction == 1:
        n_lst = [lst[len(lst) - 1]] + lst[:len(lst) - 1]
        return n_lst
    else:
        n_lst = lst[1:len(lst)] + [lst[0]]
        return n_lst

# 왼쪽과 오른쪽 톱니바퀴를 받아서 톰니바퀴가 돌 방향을 구하는 함수
def turnDirection(left_gear, right_gear, od):
    if left_gear[2] != right_gear[6]:
        return -od
    else:
        return 0

# 톱니바퀴 리스트와 방향 리스트를 받아서 방향대로 돌린 리스트를 반환하는 함수
def turnGears(g_lst, d_lst):
    for g in range(1, len(g_lst)):
            if d_lst[g]:
                g_lst[g] = turn(g_lst[g], d_lst[g])
    
    return g_lst


gear1 = list(map(int, input()))
gear2 = list(map(int, input()))
gear3 = list(map(int, input()))
gear4 = list(map(int, input()))

gears = [[0], gear1, gear2, gear3, gear4]

K = int(input())
for i in range(K):
    # 회전시킬 톱니바퀴 번호, 방향(1: 시계방향, -1: 반시계방향)
    sg, d = map(int, input().split())
    # 기어들이 돌 방향을 저장할 배열
    gear_dis = [0] * 5
    # 회전시킬 톱니바퀴의 방향 저장
    gear_dis[sg] = d

    # 회전시킬 톱니바퀴 번호에 따라
    if sg == 1:
        for gn in range(2, len(gears)):
            # 현재 기어와 왼쪽에 있는 기어를 비교해서 방향 구하기
            gear_dis[gn] = turnDirection(gears[gn-1], gears[gn], gear_dis[gn-1])
            # 현재 기어가 움직이지 않으면 그 옆 기어도 움직이지 않으므로 더이상 구하지 않음
            if gear_dis[gn] == 0:
                break
        
    elif sg == 2:
        for gn in range(3, len(gears)):
            gear_dis[gn] = turnDirection(gears[gn-1], gears[gn], gear_dis[gn-1])
            if gear_dis[gn] == 0:
                break
       
        gear_dis[1] = turnDirection(gears[1], gears[sg], gear_dis[sg])

    elif sg == 3:
        for gn in range(len(gears) - 3, 0, -1):
            gear_dis[gn] = turnDirection(gears[gn], gears[gn+1], gear_dis[gn+1])
            if gear_dis[gn] == 0:
                break

        gear_dis[4] = turnDirection(gears[sg], gears[4], gear_dis[sg])

    else:
        for gn in range(len(gears) - 2, 0, -1):
            gear_dis[gn] = turnDirection(gears[gn], gears[gn+1], gear_dis[gn+1])
            if gear_dis[gn] == 0:
                break
        
    gears = turnGears(gears, gear_dis)

total = 0
for k in range(1, len(gears)):
    total += gears[k][0] * (2 ** (k-1))

print(total)