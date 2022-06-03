import sys


N = int(input())
people = []

for _ in range(N):
    data = list(sys.stdin.readline().split())
    data[1] = int(data[1])
    data[2] = int(data[2])
    data[3] = int(data[3])
    people.append(data)

people.sort(key=lambda x: (x[3], x[2], x[1]))

print(people[-1][0])
print(people[0][0])