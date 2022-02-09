# # 버블소트

# num = int(input())
# rlt = [0] * num

# for t in range(num):
#     rlt[t] = int(input())
# for i in range(num - 1, 0, -1):
#     for j in range(i):
#         if rlt[j] > rlt[j + 1]:
#             rlt[j], rlt[j + 1] = rlt[j + 1], rlt[j]

# for k in rlt:
#     print(k)


# 카운팅 소트
num = int(input())
rlt_p = []
rlt_m = []

for _ in range(num):
    a =  int(input())
    if a < 0:
        rlt_m.append(-a)
    else:
        rlt_p.append(a)

final_p = [0] * len(rlt_p)
final_m = [0] * len(rlt_m)

if rlt_p:
    cnt_p = [0] * (max(rlt_p) + 1)
    for i in range(len(rlt_p)):
        cnt_p[rlt_p[i]] += 1

    for i in range(1, max(rlt_p) + 1):
        cnt_p[i] += cnt_p[i - 1]

    for i in range(len(rlt_p) - 1, -1, -1):
        cnt_p[rlt_p[i]] -= 1
        final_p[cnt_p[rlt_p[i]]] = rlt_p[i]

if rlt_m:
    cnt_m = [0] * (max(rlt_m) + 1)

    for i in range(len(rlt_m)):
        cnt_m[rlt_m[i]] += 1


    for i in range(1, max(rlt_m) + 1):
        cnt_m[i] += cnt_m[i - 1]


    for i in range(len(rlt_m) - 1, -1, -1):
        cnt_m[rlt_m[i]] -= 1
        final_m[cnt_m[rlt_m[i]]] = rlt_m[i]
    

for i in final_m[::-1]:
    print(-i)
for i in final_p:
    print(i)
