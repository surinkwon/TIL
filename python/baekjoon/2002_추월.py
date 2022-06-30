'''
나보다 먼저 들어온 차보다 내가 더 일찍 나가면 추월한 것
'''
import sys

N = int(input())
enter = []
exit = {}
overtake = 0

for n in range(N):
    enter.append(sys.stdin.readline().strip())

for n in range(N):
    car = sys.stdin.readline().strip()
    exit[car] = n

# 앞선 차들보다 먼저 나가는지 확인
for n in range(N - 1, 0, -1):
    car = enter[n]
    for i in range(n):
        front_car = enter[i]
        if exit[car] < exit[front_car]:
            overtake += 1
            break

print(overtake)