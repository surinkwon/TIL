s1, s2, s3 = map(int, input().split())
dice_lst = [[x for x in range(1, s1 + 1)], [x for x in range(1, s2 + 1)], [x for x in range(1, s3 + 1)]]
totals = []
for i in dice_lst[0]:
    for j in dice_lst[1]:
        for k in dice_lst[2]:
            totals.append(i + j + k)

no_dup = sorted(list(set(totals)))
min_total = 0

for total in no_dup:
    if totals.count(total) > totals.count(min_total):
        min_total = total
    else:
        break
print(min_total)