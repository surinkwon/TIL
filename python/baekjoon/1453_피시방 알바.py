# 사람 수, 앉고싶어하는 번호
num = int(input())
want = list(map(int, input().split()))
# 자리 리스트, 거절당한 횟수
seat = [0] * 101
decline = 0

for ws in want:
    seat[ws] += 1

for s in seat:
    if s > 1:
        decline += s - 1

print(decline)