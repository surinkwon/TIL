'''
문제에서는 트리를 중위순회 하는 방식으로 빌딩 이동
'''

# 중위 순회 함수, 트리 채우는 함수
def mid(node):
    global tree, n
    if node < len(tree):
        mid(node * 2)
        tree[node] = num_list[n]
        n += 1
        mid(node * 2 + 1)

K = int(input())

num_list = list(map(int, input().split()))

tree = [0] * (2 ** K)
n = 0

# 트리 채우기
mid(1)

for i in range(K + 1):
    for j in range(2 ** i, len(tree)):
        if j == 2 ** (i+1):
            break
        
        print(tree[j], end=' ')
    print()
