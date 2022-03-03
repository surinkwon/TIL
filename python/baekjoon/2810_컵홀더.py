N = int(input())
seats = input()
total = 0
c = 0

for i in range(N):
    total += 1
    if seats[i] == 'L':
        c += 1

total += (1 - c // 2) # 맨 오른쪽 컵홀더를 더해줌, 커플석은 두개를 세줬으므로 반을 빼줌

if total >= N:
    print(N)
else:
    print(total)
