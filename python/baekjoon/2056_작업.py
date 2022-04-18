'''
위상정렬
'''
from collections import deque
import sys


def howManyTime():
    global q, rlt_times, pre

    while q:
        cw = q.popleft()

        # 해당 일을 끝마치면 할 수 있는 일들을 체크
        for d in range(len(related_works[cw])):
            pre[related_works[cw][d]] -= 1

            # 다음으로 할 수 있는 일들 중 남은 선수 작업이 없는 일들은
            if pre[related_works[cw][d]] == 0:
                # 해당 작업이 끝나는 시간은 그 작업의 선수 작업 중 끝나는 시간이 가장 늦은 작업의 시간 + 해당 작업에 걸리는 시간
                for time in range(len(pre_works[related_works[cw][d]])):
                    if rlt_times[related_works[cw][d]] < rlt_times[pre_works[related_works[cw][d]][time]] + times[related_works[cw][d]]:
                        rlt_times[related_works[cw][d]] = rlt_times[pre_works[related_works[cw][d]][time]] + times[related_works[cw][d]]
                q.append(related_works[cw][d])



N = int(input())
related_works = [[] for _ in range(N + 1)]          # 그래프 정보 배열
pre_works = [[] for _ in range(N + 1)]              # 해당 일에 필요한 선 작업 정보 배열
pre = [0] * (N + 1)                                 # 선 작업 개수
times = [0] * (N + 1)                               # 각 일을 하는 데 걸리는 시간
rlt_times = [0] * (N + 1)                           # 각 일이 끝나는 시간
q = deque()

for i in range(1, N + 1):
    data = list(map(int, sys.stdin.readline().split()))
    times[i] = data[0]
    # 그래프 정보와 선 작업 정보 업데이트
    for j in range(2, len(data)):
        related_works[data[j]].append(i)
        pre_works[i].append(data[j])
    pre[i] = data[1]

    # 필요한 선수 작업이 없다면 q에 추가
    if data[1] == 0:
        q.append(i)
        rlt_times[i] = data[0]

howManyTime()

print(max(rlt_times))

