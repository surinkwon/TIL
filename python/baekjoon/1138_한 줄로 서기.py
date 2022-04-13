'''
앞에서부터 나보다 큰 사람이 들어갈 자리가 있으면 세주고
그게 내 순서랑 같으며 해당 자리가 비었으면 거기에 섬
'''

N = int(input())
lst = list(map(int, input().split()))
line = [0] * N

for i in range(N):
    cnt = j = 0
    while j < N:
        if line[j] == 0:
            if cnt == lst[i]:
                line[j] = i + 1
                break
            else:
                cnt += 1
                j += 1
        else:
            j += 1

print(' '.join([str(line[i]) for i in range(len(line))]))