# 다이얼
def sn(word):
    rlt_num = ''
    for w in word:
        if w == 'A' or w == 'B' or w == 'C':
            rlt_num += '2'
        elif w == 'D' or w == 'E' or w == 'F':
            rlt_num += '3'
        elif w == 'G' or w == 'H' or w == 'I':
            rlt_num += '4'
        elif w == 'J' or w == 'K' or w == 'L':
            rlt_num += '5'
        elif w == 'M' or w == 'N' or w == 'O':
            rlt_num += '6'
        elif w == 'P' or w == 'Q' or w == 'R' or w == 'S':
            rlt_num += '7'
        elif w == 'T' or w == 'U' or w == 'V':
            rlt_num += '8'
        elif w == 'W' or w == 'X' or w == 'Y' or w == 'Z':
            rlt_num += '9'
    
    return rlt_num

number = sn(input())
sec = 0

for n in number:
    sec += int(n) + 1

print(sec)