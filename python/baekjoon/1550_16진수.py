a = input()
b = a[::-1]
al = ['A', 'B', 'C', 'D', 'E', 'F']
total = 0
for i in range(len(b)):
    if b[i] in al:
        total += (al.index(b[i]) + 10) * (16 ** i)
    else:
        total += int(b[i]) * (16 ** i)
print(total)
