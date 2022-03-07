N = int(input())
word = [[] for _ in range(51)]

# 스택을 이용한 방식, 시간초과...
# stack = [0] * N
# t = -1

# for _ in range(N):
#     w = input()
#     if w not in stack:
#         if t == -1:
#             t += 1
#             stack[t] = w
#         else:
#             if len(w) < len(stack[t]):
#                 t += 1
#                 stack[t] = w
#             elif len(w) == len(stack[t]):
#                 i = t
#                 while i > -1 and w > stack[i]:
#                     stack[i + 1] = stack[i]
#                     i -= 1
#                 stack[i + 1] = w
#                 t += 1
#             else:
#                 i = t
#                 while i > -1 and len(w) > len(stack[i]):
#                     stack[i + 1] = stack[i]
#                     i -= 1
#                 stack[i + 1] = w
#                 tem = w

#                 while i > -1 and len(tem) >= len(stack[i]) and tem > stack[i]:
#                     stack[i + 1] = stack[i]
#                     i -= 1
#                 stack[i + 1] = w
#                 t += 1

# for k in range(t, -1, -1):
#     print(stack[k])

# 단어 길이 최대가 50이므로 row가 51개인 이차원 배열 만들고 
# 입력받은 문자열의 길이와 같은 수의 인덱스에 추가
# 각 인덱스마다 정렬하고 출력
for i in range(N):
    w = input()
    wl = len(w)
    if w not in word[wl]:
        word[wl].append(w)

for i in range(len(word)):
    if word[i]:
        word[i].sort()
        for j in range(len(word[i])):
            print(word[i][j])







