import sys

N, M = map(int, input().split())
never_saw = set()
never_saw_heard = []
for _ in range(N):
    name = sys.stdin.readline().split()[0]
    never_saw.add(name)

for _ in range(M):
    name = sys.stdin.readline().split()[0]
    if name in never_saw:
        never_saw_heard.append(name)

never_saw_heard.sort()
print(len(never_saw_heard))
for i in range(len(never_saw_heard)):
    print(never_saw_heard[i])