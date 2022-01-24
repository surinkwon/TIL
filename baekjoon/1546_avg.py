from posixpath import split

sub_num = int(input())
scores = list(map(int, input().split()))
change_score = []
max_score = max(scores)

for score in scores:
    change_score.append(score / max_score * 100)

print(sum(change_score) / sub_num)
