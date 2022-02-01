# 크로아티아 알파벳

word = input()

i = 0
total = 0
while i < len(word) - 1:
    if word[i] == 'c':
        if word[i + 1] == '=' or word[i + 1] == '-':
            total += 1
            i += 2
        else:
            total += 1
            i += 1
    elif word[i] == 'd':
        if word[i + 1] == '-':
            total += 1
            i += 2
        elif i < len(word) - 2 and word[i + 1] == 'z' and word[i + 2] == '=':
            total += 1
            i += 3
        else:
            total += 1
            i += 1
    elif word[i] == 'l' or word[i] == 'n':
        if word[i + 1] == 'j':
            total += 1
            i += 2
        else:
            total += 1
            i += 1
    elif word[i] == 's' or word[i] == 'z':
        if word[i + 1] == '=':
            total += 1
            i += 2
        else:
            total += 1
            i += 1
    else:
        total += 1
        i += 1

if word[-1] != '=' and word[-1] != '-':
    if word[-1] == 'j':
        if word[-2] != 'n' and word[-2] != 'l':
            total += 1
    else:
        total += 1

print(total)
    
