import sys

# 보성이를 지목할 수 있는 횟수를 찾는 함수
def find():
    v = [0] * N     # 지목 당한지 체크
    num = 0         # 다음 번호를 외칠 사람
    cnt = 0         # 번호를 외친 횟수

    while True:
        num = pointing[num]     # 다음 번호를 외침
        cnt += 1                # 횟수 증가

        if v[pointing[num]]:    # 이미 불린 적이 있으면 & 보성이 번호가 나오지 않았으면
            return -1           # 보성이를 부를 수 없으므로 -1 반환
        
        v[pointing[num]] = 1    # 불린 적 없으면 불렸다고 체크
        
        if num == K:            # 보성이 번호면 횟수 반환
            return cnt

N, K = map(int, input().split())    # 참가하는 사람 수, 보성이의 숫자
pointing = [0] * N                  # 각 사람들이 지목할 숫자들

for i in range(N):
    pointing[i] = int(sys.stdin.readline())

rlt = find()
print(rlt)
