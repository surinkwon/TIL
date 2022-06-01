words = []
for _ in range(5):
    words.append(input())

max_len = max(len(words[0]), len(words[1]), len(words[2]), len(words[3]), len(words[4]))

rlt = ''

for ml in range(max_len):
    for i in range(5):
        if len(words[i]) - 1 >= ml:
            rlt += words[i][ml]

print(rlt) 