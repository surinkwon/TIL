N, L, D = map(int, input().split())
# 앨범 재생이 끝나는 시간
finish = N * L + (N - 1) * 5

# 전화벨 리스트, 인덱스를 초와 동기화 시키기 위해 +1
phone_ring = [0] * (finish + 1)
for i in range(len(phone_ring)):
    if i % D == 0:
        phone_ring[i] = 1

# 노래 리스트
album = [1] * (finish + 1)
j = 0
while j < len(album):
    j += L
    for s in range(5):
        if j + s < len(album):
            album[j + s] = 0
    j += 5



for second in range(1, len(album) + 1):
    # 앨범이 끝났는데도 전화를 받지 못했으면 앨범이 끝난 초 // 전화벨 울리는 시간 + 1 * 전화벨 울리는 시간
    # 앨범이 끝난 초를 전화벨이 울리는 시간으로 나눠 몫을 취하면 그것이 앨범이 재생되는 동안 전화벨이 몇번 울렸는지가 됨
    # 거기에 전화벨이 울리는 시간을 곱해주면 앨범이 끝나고 처음으로 전화벨이 울리는 시간이 됨
    if second == len(album):
        print((((finish + 1) // D) + 1) * D)
        break

    # 노래가 꺼져있을 때 전화가 울리면 출력
    if album[second] == 0 and phone_ring[second] == 1:
        print(second)
        break



