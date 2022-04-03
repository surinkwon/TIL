'''
덱을 이용
그냥 그대로 구현
'''


from collections import deque


N, K = map(int, input().split())
du = list(map(int, input().split()))
for i in range(len(du)):
    du[i] = [du[i], 0, i]
conveyor = deque(du)
stage = 0
no_du = set()

while True:
    stage += 1
# 벨트가 로봇과 함께 회전
    conveyor.appendleft(conveyor.pop())
    # 만약 로봇이 내리는 칸에 왔으면 내림
    if conveyor[N-1][1]:
        conveyor[N-1][1] = 0

# 로봇이 한 칸 앞으로 이동(이동할 수 있으면: 앞 칸의 내구도가 1이상 남아있으며 로봇이 없으면)
    for i in range(N - 1, 0, -1):
        if conveyor[i][1] == 0 and conveyor[i-1][1] and conveyor[i][0]:
            conveyor[i][0] -= 1
            conveyor[i][1] = 1
            conveyor[i-1][1] = 0
        
        if conveyor[i][0] == 0 and conveyor[i][2] not in no_du:
                no_du.add(conveyor[i][2])
    
    if conveyor[N-1][1]:
        conveyor[N-1][1] = 0

# 올리는 위치 칸의 내구도가 0이 아니면 로봇 올림
    if conveyor[0][0]:
        conveyor[0][0] -= 1
        conveyor[0][1] = 1
        if conveyor[0][0] == 0 and conveyor[0][2] not in no_du:
                no_du.add(conveyor[0][2])
    

# 내구도가 0인 칸 개수가 K개 이상이면 종료
    if len(no_du) >= K:
        break

print(stage)