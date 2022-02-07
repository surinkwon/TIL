# 알파벳 찾기
word = input()
num = []
alph = 'abcdefghijklmnopqrstuvwxyz'

for i in alph:
    num.append(str(word.find(i)))
print(' '.join(num))
