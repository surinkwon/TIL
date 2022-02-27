import sys

sys.stdin = open('input.txt')

T = int(input())


# 창고에서 화학물질 용기를 찾는 함수
def isChem(matrix, r, c):
    width = length = 0
    i = 0
    
    # 인덱스 범위 내에서 가로와 세로를 구함
    while i < len(matrix) - r and matrix[r + i][c]:
        row = r + i
        j = 0
        while j < len(matrix) - c and matrix[r + i][c + j]:
            col = c + j
            if matrix[row][col]:
                matrix[row][col] = 0 # 중복으로 세는 것을 방지하기 위한 조치
                width = j + 1
                j += 1
        length = i + 1
        i += 1

    size = width * length

    return length, width, size


# 찾은 용기들을 행 크기를 기준으로 정렬하는 함수
def rowSort(lst, sizes):
    for i in range(len(lst) - 1, 0, -1):
        for j in range(i):
            if lst[j][0] > lst[j + 1][0]:
                temp = lst[j]
                lst[j] = lst[j + 1]
                lst[j + 1] = temp

                temp = sizes[j]
                sizes[j] = sizes[j + 1]
                sizes[j + 1] = temp

    return lst, sizes

# 찾은 용기들을 크기별로 정렬하는 함수
def sizeSort(lst, sizes):
    for i in range(len(sizes) - 1, 0, -1):
        for j in range(i):
            if sizes[j] > sizes[j + 1]:
                temp = sizes[j]
                sizes[j] = sizes[j + 1]
                sizes[j + 1] = temp

                temp = lst[j]
                lst[j] = lst[j + 1]
                lst[j + 1] = temp

    return lst, sizes


for tc in range(1, T + 1):
    N = int(input()) # 창고 너비
    storage = [list(map(int, input().split())) for _ in range(N)]
    chems = []
    chems_size = []
    total = 0
    
    # 화학물질이 들어있으면 용기 크기를 찾음
    for i in range(len(storage)):
        for j in range(len(storage[i])):
            if storage[i][j]:
                leng, wid, size = isChem(storage, i, j)
                chems.append((leng, wid))
                chems_size.append(size)
                total += 1
    
    # 용기들을 행 길이대로 정렬 후 사이즈별로 재정렬함
    chems, chems_size = rowSort(chems, chems_size)
    chems, chems_size = sizeSort(chems, chems_size)
    
    # 출력을 위한 리스트 만들기
    rlt = [0] * (len(chems) * 2)
    num = 0
    for i in range(len(chems)):
        l, w = chems[i]
        rlt[num] = l
        rlt[num + 1] = w
        num += 2

    print(f'#{tc} {total} {" ".join([str(x) for x in rlt])}')

