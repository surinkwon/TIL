'''
문제를 잘 읽자.
문제에서는 나보다 덩치 큰 사람의 수 + 1이 내 순위가 된다고 했는데
덩치의 우위를 가릴 수 없는 경우는 모두 랭크가 같다고 이해하니 풀리지가 않았다.
'''

N = int(input())
# 몸무게, 키, 순위를 담을 리스트
people = [[0] * 3 for _ in range(N)]

# 사람들 정보를 저장
for i in range(len(people)):
    w, h = map(int, input().split())
    people[i][0] = w
    people[i][1] = h

# 리스트를 돌며 나보다 덩치가 큰 사람 수를 찾고 내 순위 갱신
for i in range(len(people)):
    rank = 1
    for j in range(len(people)):
        if i != j:
            if people[i][0] < people[j][0] and people[i][1] < people[j][1]:
                rank += 1
        
        people[i][2] = rank

# 순위만 결과 리스트에 따로 저장
# 2차원 리스트라 얕은 복사가 일어나서 w배열에서의 순위값을 변동시키면 people의 값도 바뀜
# 따라서 처음에 데이터가 들어온 순서대로의 덩치 순위를 알 수 있음
rlt = [0] * len(people)
for j in range(len(people)):
    rlt[j] = str(people[j][2])

print(' '.join(rlt))

