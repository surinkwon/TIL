h, m, s = map(int, input().split())
process_s = int(input())

if s + process_s> 59:
    m += (s + process_s) // 60
    s = (s + process_s) % 60
else:
    s += process_s

if m > 59:
    h += m // 60
    m %= 60

if h > 23:
    h %= 24

print(f'{h} {m} {s}')