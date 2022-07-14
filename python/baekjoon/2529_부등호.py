'''
백트래킹
조건지정을 잘 하는 것이 중요
'''
def findNum(i, N, number):
    global num, answers
    if i == N:
        answers.append(number)
    else:
        for v in range(10):
            if i == 0:
                num[v] = 1
                findNum(i+1, N, number+str(v))
                num[v] = 0
            elif i > 0 and num[v] == 0:
                if inequality_sign[i-1] == '>' and int(number[i-1]) > v:
                    num[v] = 1
                    findNum(i+1, N, number+str(v))
                    num[v] = 0
                elif inequality_sign[i-1] == '<' and int(number[i-1]) < v:
                    num[v] = 1
                    findNum(i+1, N, number+str(v))
                    num[v] = 0
            

K = int(input())

inequality_sign = list(input().split())
num = [0] * 10
answers = []

findNum(0, K+1, '')
print(answers[-1])
print(answers[0])