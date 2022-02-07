num = int(input())
fst = []
s = []
for _ in range(num):
    first_name = input()
    fst.append(first_name[0])

for first_letter in fst:
    if fst.count(first_letter) > 4 and (first_letter not in s):
        s.append(first_letter)

if s:
    s.sort()
    print(''.join(s))
else:
    print('PREDAJA')