n = int(input())
word = input()

# 암호화 할 때 사용하는 행렬을 만들어서 복원
table = [[0] * n for _ in range(len(word)//n)]

word_index = 0
while word_index < len(word):
    for i in range(len(table)):
        for j in range(n):
            table[i][j + ((n - 1 - 2 * j) * (i % 2))] = word[word_index]
            word_index += 1

rlt = ''
for j in range(n):
    for i in range(len(table)):
        rlt += table[i][j]

print(rlt)