import sys

sys.stdin = open('input.txt')

T = 10

# 중위 순회 함수
def inOrder(t, s):
    if s < len(t):
        fst = inOrder(t, s*2)
        scd = t[s]
        lst = inOrder(t, s*2+1)
        
        # 노드에서 왼쪽 노드가 없거나 오른쪽 노드가 없거나 둘 다 없을 수 있으므로
        # 모두 고려
        if fst and lst:
            return fst+scd+lst
        elif fst:
            return fst+scd
        elif lst:
            return scd+lst
        else:
            return scd


for tc in range(1, T + 1):
    # 정점 개수 입력받고 각 정점에 해당하는 알파벳 입력받기
    N = int(input())
    tree = [0] * (N + 1)
    children = [0] * (N + 1)
    
    # 글자 뒤에 들어오는 숫자 처리하며 트리에 추가
    for i in range(N):
        if i <= N // 2:
            node, c, *ch = input().split()
        else:
            node, c = input().split()
        node = int(node)
        tree[node] = c
        children[node] = ch

    # 트리 중위순회
    rlt = inOrder(tree, 1)

    print(f'#{tc} {rlt}')

