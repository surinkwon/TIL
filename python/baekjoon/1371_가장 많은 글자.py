import sys

sys.stdin = open('input.txt')

# DAT
dat = [0] * 130
rlt = ''

# 문자열
sentence = sys.stdin.read()

# 문자 개수
for i in sentence:
    dat[ord(i)] += 1

for j in range(97, len(dat)):
    if dat[j] == max(dat[97:]):
        rlt += chr(j)

# 최종 출력
print(rlt)
