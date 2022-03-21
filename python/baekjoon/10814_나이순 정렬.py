import sys

# sort()를 사용하면 쉽게 풀 수 있음

N = int(input())
people = [0] * N

# 사람들 데이터 정보를 저장
for i in range(len(people)):
    age, name = sys.stdin.readline().split()
    age = int(age)
    people[i] = [age, name]

# 나이순으로 정렬
people.sort(key=lambda x:x[0])

for i in range(len(people)):
    print(f'{people[i][0]} {people[i][1]}')