# 숫자의 합
a = int(input())
b = input()
c = [j for j in b]

total = 0

for i in range(a):
    total += int(c[i])

print(total)