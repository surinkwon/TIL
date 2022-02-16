import sys

sys.stdin = open('s_input.txt')

T = int(input())


for tc in range(1, T + 1):
    # 버스 노선 수
    num = int(input())
    # 버스 노선을 받음
    a = [0] * num
    b = [0] * num

    for i in range(num):
        a[i], b[i] = map(int, input().split())

    # 정류장의 수
    bus_stop_n = int(input())

    bus_stop = [0] * bus_stop_n
    for j in range(bus_stop_n):
        bus_stop[j] = int(input())

    rlt = [0] * bus_stop_n
    k = 0

    # 각 정류장에 몇 개의 버스 노선이 지나는 지 확인
    while k < len(bus_stop):
        for l in range(len(a)):
            if a[l] <= bus_stop[k] <= b[l]:
                rlt[k] += 1
        k += 1 # while 쓸 때는 항상 무한루프 안 돌게 조건 붙여주기

    print(f'#{tc} {" ".join([str(x) for x in rlt])}')

