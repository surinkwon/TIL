N = int(input()) # 줄 선 사람 수
times = list(map(int, input().split()))

# 시간이 적은 순서대로 앞에 서야하므로 카운팅소트로 정렬
time_dat = [0] * (max(times) + 1)
rlt = [0] * len(times)
for i in range(len(times)):
    time_dat[times[i]] += 1

for i in range(1, len(time_dat)):
    time_dat[i] += time_dat[i-1]
    
for i in range(len(times)):
    time_dat[times[i]] -= 1
    rlt[time_dat[times[i]]] = times[i]

# 정렬된 시간들의 누적합을 구하면 각각의 사람들이 걸리는 시간이 됨
for i in range(1, len(rlt)):
    rlt[i] += rlt[i-1]

# 그걸 모두 더해주면 결과값
print(sum(rlt))