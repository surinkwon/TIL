import heapq
import sys

heap = []

N = int(input())

for _ in range(N):
    data = int(sys.stdin.readline())
    if data:
        heapq.heappush(heap, data)
    else:
        if len(heap):
            print(heapq.heappop(heap))
        else:
            print(0)