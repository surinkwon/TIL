import sys
# 각 줄 중량을 정렬하고 최소부터 계산해나감
# 들 수 있는 중량의 값은 가장 작은 중량 * 로프 개수이기 때문에

N = int(input())
w = [0] * N
tw = [0] * N

for i in range(N):
    w[i] = int(sys.stdin.readline())

w.sort()

for i in range(N):
    tw[i] = w[i] * (len(w) - i)

print(max(tw))