import sys

sys.stdin = open('input.txt')

'''
오타 주의
리스트 안에 숫자 원소가 들어있으면 길이를 셀 수 없다는 것을 기억
입력 받을 때 제대로 입력받기
'''


T = 10

# 후위 순회하며 연산하는 함수
def postOrder(tree, node):
    if len(tree[node]) == 3:
        left = postOrder(tree, tree[node][1])
        right = postOrder(tree, tree[node][2])
        op = tree[node][0]

        if op == '+':
            return left + right
        elif op == '-':
            return left - right
        elif op == '*':
            return left * right
        else:
            return left / right
    else:
        return tree[node][0]


for tc in range(1, T + 1):
    N = int(input())
    tree = [0] * 1001

    # 트리 채우기
    for _ in range(N):
        lst = list(input().split())
        p = int(lst[0])
        
        # 연산자가 값으로 들어올 때
        if len(lst) == 4:
            lc, rc = int(lst[2]), int(lst[3])
            tree[p] = (lst[1], lc, rc)
        # 숫자가 값으로 들어올 때
        else:
            tree[p] = [int(lst[1])]

    # 후위 순회하며 계산
    rlt = int(postOrder(tree, 1))

    print(f'#{tc} {rlt}')

