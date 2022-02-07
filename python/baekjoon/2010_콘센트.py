import sys
t = int(sys.stdin.readline())
total = 0
for _ in range(t):
    total += int(sys.stdin.readline())
print(total - t + 1)
