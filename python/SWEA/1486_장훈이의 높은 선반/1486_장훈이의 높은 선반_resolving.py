import sys

sys.stdin = open('input.txt')

T = int(input())

'''
부분집합 구할 때처럼 풀 필요는 없음
부분집합처럼 원소가 무엇인지 알 필요가 없기 때문에 그냥 해당 직원 키를 더할지 안 더할지만 정해주면 됨
'''
def DFS(i, n, s):
    global min_tall
    if i == n:
        if s >= B:
            if min_tall > s - B:
                min_tall = s - B
    elif s > B and s - B > min_tall:
        return
    else:
        DFS(i+1, n, s)
        DFS(i+1, n, s+clerk[i])

for tc in range(1, T + 1):
    N, B = map(int, input().split())
    clerk = list(map(int, input().split()))
    min_tall = 987654321

    DFS(0, len(clerk), 0)

    print(f'#{tc} {min_tall}')