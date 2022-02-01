# 단어 공부

word = input()

w_lst = [ord(x) for x in word]

for i in range(len(w_lst)):
    if w_lst[i] >= 97:
        w_lst[i] -= 32

w = []
for j in w_lst:
    if j not in w:
        w.append(j)

w_num = []
for k in w:
    w_num.append(w_lst.count(k))

if w_num.count(max(w_num)) >= 2:
    print('?')
else:
    print(chr(w[w_num.index(max(w_num))]))
