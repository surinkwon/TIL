N, W, L = map(int, input().split())
trucks = list(map(int, input().split()))

q = [(trucks[0], 1)]
front = 0
cw = trucks[0]
time = 1
ti = 1

while front < len(q):
    time += 1
    # 트럭 내리기
    if q[front][1] + W == time:
        cw -= q[front][0]
        front += 1

    # 트럭 올리기
    if ti < len(trucks) and cw + trucks[ti] <= L:
        cw += trucks[ti]
        q.append((trucks[ti], time))
        ti += 1

print(time)