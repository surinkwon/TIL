# # 가장 사전적으로 앞서는 문자의 인덱스를 찾는 함수
# def first(word):
#     idx = len(word) - 1
#     letter = word[len(word) - 1]
#     for i in range(len(word) - 1, -1, -1):
#         if letter > word[i]:
#             letter = word[i]
#             idx = i
#     return idx + 1

# # 문자열 뒤집는 함수
# def reverseWord(word):
#     rlt = ''
#     for i in range(len(word)):
#         rlt = word[i] + rlt
    
#     return rlt

# word = input()

# if len(word) == 3:
#     print(word)
# else:
#     # 단어 뒤에서부터 가장 사전적으로 앞서는 문자의 인덱스를 구함
#     fw = word[:first(word[:len(word)-2])]

#     # 그 인덱스까지 단어를 자르고 그 뒤부터 다시 같은 행위 반복
#     sw = word[len(fw):][:first(word[len(fw):len(word) - 1])]
#     tw = word[len(fw) + len(sw):]
#     print(reverseWord(fw) + reverseWord(sw) + reverseWord(tw))
# 위에는 처음 풀이 근데 저렇게하면 bacadd같은 경우가 답과 다름

word = input()
rlt = 'z' * 50
for i in range(1, len(word) - 1):
    for j in range(i + 1, len(word)):
        fw = word[:i]
        sw = word[i:j]
        lw = word[j:]
        nw = fw[::-1] + sw[::-1] + lw[::-1]
        if rlt > nw:
            rlt = nw

print(rlt)


