# 이름 개수 
n = int(input())

# 이름을 담을 배열, 출력할 문자
words = [0] * n
for i in range(n):
    words[i] = input()
rlt = ''

if n != 1: # n이 1이면 for문에서 word인덱스 참조 불가
    # 배열을 돌며 이름들을 비교
    for letter in range(len(words[0])):
        for word in range(1, n):
            # 하나라도 다르면 물음표 추가하고 반복문 빠져나옴
            if words[word][letter] != words[word - 1][letter]:
                rlt += '?'
                break
        # 모두 같으면 해당 문자를 추가
        else:
            rlt += words[word][letter]
    print(rlt)
else:
    print(words[0])
