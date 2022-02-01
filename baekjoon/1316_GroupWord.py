# 그룹 단어 체커
def wc(letter, word):
    ch = None
    if word.count(letter) >= 2:
        for i in range(1, word.count(letter)):
            if word[word.index(letter) + i] == letter:
                ch = True
            else:
                ch = False
                break
    else:
        ch = True
    return ch


num = int(input())
total = 0

for _ in range(num):
    word = input()
    for l in word:
        rlt = wc(l, word)
        
        if rlt == False:
            break
    if rlt == True:
        total += 1

print(total)


