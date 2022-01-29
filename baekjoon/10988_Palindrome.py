# 펠린드롬인지 확인하기
w = input()

def palin(word):

    if len(word) < 2:
        return 1
    
    if word[0] == word[-1]:
        return palin(word[1:-1])
    else:
        return 0

print(palin(w))