M, N = map(int, input().split())
cut_num = int(input())
row_cut = [0, N]
col_cut = [0, M]

for _ in range(cut_num):
    data = list(map(int, input().split()))
    if data[0]:
        col_cut.append(data[1])
    else:
        row_cut.append(data[1])

max_area = 0
row_cut.sort()
col_cut.sort()

for r in range(1, len(row_cut)):
    height = row_cut[r] - row_cut[r-1]
    for c in range(1, len(col_cut)):
        width = col_cut[c] - col_cut[c-1]
        if max_area < height * width:
            max_area = height * width

print(max_area)
