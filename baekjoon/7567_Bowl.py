# 그릇
a = input()
total = 10

for b in range(1, len(a)):
    if a[b-1] == a[b]:
        total += 5
    else:
        total += 10

print(total)