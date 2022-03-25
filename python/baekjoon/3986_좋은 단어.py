'''
괄호검사와 비슷하면서도 다른 점은 둘다 스택을 이용하지만
이 문제는 짝이 맞는지를 진행하면서 구분해낼 수 없다는 점이다.
괄호는 () 이렇게 짝이 있지만 이 문제에서 단어는 A, B밖에 없으므로
A와 다른 A가 짝이 맞는 것인지 아닌지를 중간에 판별해낼 수 없다.

따라서 단어의 끝까지 돌면서 스택에 넣고 빼는 연산을 하고난 후에야
이 단어가 좋은 단어인지 아닌지를 알 수 있다.
'''

# 스택을 이용해 좋은 단어인지 검사하는 함수
def isGoodWord(word):
    stack = [0] * len(word)
    top = 0
    stack[top] = word[0]

    for i in range(1, len(word)):
        if word[i] != stack[top]:
            top += 1
            stack[top] = word[i]
        else:
            top -= 1
    
    if top == -1:
        return 1
    else:
        return 0
    
    
N = int(input())
cnt = 0
for _ in range(N):
    string = input()
    if len(string) % 2 == 0:
        cnt += isGoodWord(string)

print(cnt)