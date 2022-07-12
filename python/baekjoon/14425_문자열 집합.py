import sys

N, M = map(int, input().split())
string_set = set()
total = 0

for _ in range(N):
    string_set.add(sys.stdin.readline().strip())

for _ in range(M):
    string = sys.stdin.readline().strip()
    if string in string_set:
        total += 1

print(total)