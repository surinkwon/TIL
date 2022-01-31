# 셀프 넘버

def self_number(num):
    if num < 10:
        return num + num
    elif num < 100:
        return num + num // 10 + num % 10
    elif num < 1000:
        return num + num // 100 + (num % 100) // 10 + (num % 100) % 10
    else:
        return num + num // 1000 + (num % 1000) // 100 + ((num % 1000) % 100) // 10 + ((num % 1000) % 100) % 10

a = [x for x in range(1, 10001)]
b = a[:]

for i in a[:len(a) - 1]:
    c = self_number(i)
    if c in b:
        b.remove(c)

for j in b:
    print(j)