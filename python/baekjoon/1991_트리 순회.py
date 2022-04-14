def preorder(node):
    if node:
        print(chr(node+64), end='')
        preorder(tree[node][0])
        preorder(tree[node][1])

def midorder(node):
    if node:
        midorder(tree[node][0])
        print(chr(node+64), end='')
        midorder(tree[node][1])

def postorder(node):
    if node:
        postorder(tree[node][0])
        postorder(tree[node][1])
        print(chr(node+64), end='')


N = int(input())
tree = [[0, 0] for _ in range(N+1)]
tree[0] = 0

# 트리 만들기
for _ in range(N):
    p, c1, c2 = input().split()
    if 'A' <= c1 <= 'Z':
        tree[ord(p) - 64][0] = ord(c1) - 64
    if 'A' <= c2 <= 'Z':
        tree[ord(p) - 64][1] = ord(c2) - 64
    
preorder(1)
print()
midorder(1)
print()
postorder(1)