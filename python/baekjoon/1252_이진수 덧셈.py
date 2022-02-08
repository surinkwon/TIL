# a, b = map(lambda x: int(x, 2), input().split())
# print(bin(a+b)[2:])

a, b = input().split()
num1 = a[::-1]
num2 = b[::-1]
n1 = 0
n2 = 0

for i in range(len(num1)):
    n1 += int(num1[i]) * (2 ** i)
for i in range(len(num2)):
    n2 += int(num2[i]) * (2 ** i)

total = n1 + n2

print(bin(total)[2:])