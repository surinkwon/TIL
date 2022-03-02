N = int(input())
draw = list(map(int, input().split()))
line = [0] * N

# 1번학생은 무조건 맨 앞
line[0] = 1

# 2번학생부터는 번호 - 1의 인덱스가 원래 자신의 위치인데
# 0보다 높은 숫자를 뽑으면 그 수만큼 현재 맨 뒤에 있는 사람을 뒤로 당기고
# 자신이 끝 인덱스에서 뽑은 번호만큼 앞으로 가서 줄을 섬
for i in range(1, N):
    for j in range(i, i - draw[i], -1):
        line[j] = line[j - 1]
    line[i - draw[i]] = i + 1

print(' '.join([str(x) for x in line]))
