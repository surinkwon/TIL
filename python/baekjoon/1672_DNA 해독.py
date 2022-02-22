# 염기서열 표, 염기서열 딕셔너리
DNA = [['A', 'C', 'A', 'G'], ['C', 'G', 'T', 'A'], ['A', 'T', 'C', 'G'], ['G', 'A', 'G', 'T']]
DNA_order = {'A': 0, 'G': 1, 'C': 2, 'T': 3}

N = int(input())
word = list(input())

for i in range(len(word) - 2, -1, -1):
    word[i] = DNA[DNA_order[word[i]]][DNA_order[word[i + 1]]]

print(word[0])
