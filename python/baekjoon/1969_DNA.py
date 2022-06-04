N, M = map(int, input().split())
DNA = [''] * N
hd = [0] * N
rlt = ''
rlt_num = 0

for i in range(N):
    DNA[i] = input()

for i in range(M):
    dna_lst = ['A', 'C', 'G', 'T']
    dna_num_lst = [0] * 4

    for j in range(N):
        dna_num_lst[dna_lst.index(DNA[j][i])] += 1
    
    max_dna = ''
    max_dna_num = 0
    for d in range(4):
        if max_dna_num < dna_num_lst[d]:
            max_dna_num = dna_num_lst[d]
            max_dna = dna_lst[d]
    rlt += max_dna
    rlt_num += N - max_dna_num

print(rlt)
print(rlt_num)

