doc = input()
search = input()

# 그냥 패턴찾기 하면 됨
i = j = cnt = 0
while i + j < len(doc):
    if doc[i+j] == search[j]:
        j += 1
    else:
        i += 1
        j = 0
    
    if j == len(search):
        cnt += 1
        i += j
        j = 0

print(cnt)