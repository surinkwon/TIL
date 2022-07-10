N = int(input())

extentions = {}

for _ in range(N):
    file_name, extention = list(input().split('.'))
    if not extentions.get(extention):
        extentions[extention] = 1
    else:
        extentions[extention] += 1

extentions_lst = []

for k, v in extentions.items():
    extentions_lst.append([k, v])

extentions_lst.sort()

for i in range(len(extentions_lst)):
    print(extentions_lst[i][0], extentions_lst[i][1])