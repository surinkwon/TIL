import heapq
import sys

N = int(input())
heap = []
for _ in range(N):
    op = int(sys.stdin.readline())
    if op == 0:
        if heap:
            print(-heapq.heappop(heap))
        else:
            print(0)
    else:
        heapq.heappush(heap, -op)