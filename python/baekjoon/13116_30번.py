'''
트리
포화 이진 트리에서 부모 노드 번호는 자식 노드 번호 // 2
'''

T = int(input())

for _ in range(T):
    a, b = map(int, input().split())

    big_n = max(a, b)
    small_n = min(a, b)
    nodes = set()
    rlt = 0

    while small_n > 0:
        nodes.add(small_n)
        small_n //= 2
    
    while big_n > 0:
        big_n //= 2
        if big_n in nodes:
            rlt = big_n
            break
    
    print(10*rlt)
