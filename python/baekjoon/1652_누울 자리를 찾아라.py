N = int(input())
room = [list(input()) for _ in range(N)]
total_r = total_c = 0

for i in range(len(room)):
    for j in range(len(room[i])):
        rcnt = ccnt = 0
        # 가로 검사
        if room[i][j] == '.':
            # 어중간하게 눕는 경우 제외
            if j - 1 < 0 or room[i][j-1] == 'X':
                for d in range(len(room)):
                    if j + d < len(room[i]):
                        if room[i][j+d] == '.':
                            rcnt += 1
                        else:
                            break # 중간에 짐이나 벽 만나면 그만 셈
                if rcnt > 1:
                    total_r += 1

        # 세로 검사
        if room[j][i] == '.':
            # 어중간하게 눕는 경우 제외
            if j - 1 < 0 or room[j-1][i] == 'X':
                for d in range(len(room)):
                    if j + d < len(room[i]):
                        if room[j+d][i] == '.':
                            ccnt += 1
                        else:
                            break # 중간에 짐이나 벽 만나면 그만 셈
                if ccnt > 1:
                    total_c += 1
                
print(f'{total_r} {total_c}')
