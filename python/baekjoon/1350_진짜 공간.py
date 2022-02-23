# 파일 개수, 파일 크기 리스트, 클러스터 크기
Num = int(input())
file = list(map(int, input().split()))
cluster = int(input())
total = 0

for i in range(Num):
# 파일크기가 0이면 클러스터 차지 안 함
    if file[i] == 0:
        continue
# 파일 크기가 클러스터 크기보다 작거나 같으면 클러스터 크기만큼 공간차지
    elif file[i] <= cluster:
        total += cluster

# 파일 크기가 클러스터 크기보다 크면
    else:
# 파일 크기가 클러스터 크기의 배수가 아니면 (파일 크기 // 클러스터 크기 + 1) * 클러스터 크기만큼 차지
        if file[i] % cluster:
            total += (file[i] // cluster + 1) * cluster
# 파일크기가 클러스터 크기의 배수면 (파일 크기 // 클러스터 크기) * 클러스터 크기만큼 공간 차지
        else:
            total += (file[i] // cluster) * cluster
print(total)


