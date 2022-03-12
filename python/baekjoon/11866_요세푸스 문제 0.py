'''
그냥 while문으로만 구현하려고 하면 시간초과가 난다. 메소드를 써주면 더 빨리 풀 수 있다.
리스트는 인덱스가 0부터 시작하기 때문에 K-1 한 값을 더해서 그 인덱스 값을 결과 리스트에 저장한다.
그 후 앉아있던 번호 리스트에서 빠진 사람을 제거한다. 
% num을 해주는 이유는 c_id가 증가함에 따른 인덱스 에러를 방지하기 위한 것
리스트에서 사람이 빠지면 인덱스 범위도 변화하니 num 값도 줄여준다.
'''

N, K = map(int, input().split())
num = N
circle = [i + 1 for i in range(N)]
rlt = [0] * N

c_id = rlt_id = 0

while rlt_id < len(rlt):
    if num > 0:
        c_id = (c_id + (K - 1)) % num

    rlt[rlt_id] = circle[c_id]
    circle.remove(circle[c_id])
    rlt_id += 1
    num -= 1

print(f'<{", ".join([str(x) for x in rlt])}>')