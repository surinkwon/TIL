a = list(input())
b = list(input())
id = len(b)
cnt = 0

for i in range(len(a)):
    for j in range(id - cnt):
        if a[i] == b[j]:
            cnt += 1
            b.remove(b[j])
            break

print(len(a) + len(b) - cnt)