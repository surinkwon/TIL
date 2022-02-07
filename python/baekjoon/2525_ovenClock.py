h, m = map(int, input().split())
process_m = int(input())

if m + process_m >= 60:
    h += (m + process_m) // 60
    m = (m + process_m) % 60
else:
    m += process_m

if h > 23:
    h %= 24

print(f'{h} {m}')