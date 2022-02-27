alph = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9, 'K': 10, 'L': 11, 'M': 12, 'N': 13, 'O': 14
, 'P': 15, 'Q': 16, 'R': 17, 'S': 18, 'T': 19, 'U': 20, 'V': 21, 'W': 22, 'X': 23, 'Y': 24, 'Z': 25}
N = int(input())

for _ in range(N):
    rlt = 'not nice'
    word, num = input().split('-')
    word_num = (26 ** 2) * alph[word[0]] + 26 * alph[word[1]] + alph[word[2]]
    num_num = int(num)

    rlt_num = word_num - num_num 

    if -100 <= rlt_num <= 100 :
        rlt = 'nice'
    print(rlt)

