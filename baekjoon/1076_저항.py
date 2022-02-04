color_lst = ['black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'violet', 'grey', 'white']
color = []
rlt = ''
for _ in range(3):
    color.append(input())

for i in range(3):
    if color[i] in color_lst:
        if i < 2:
            rlt += str(color_lst.index(color[i]))
        else:
            rlt = int(rlt) * (10 ** color_lst.index(color[i]))

print(rlt)

