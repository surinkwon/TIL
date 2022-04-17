'''
그냥 구현하면 되는데 반례를 잘 생각해볼 것
'''


import sys
from collections import deque

T = int(input())


def ins(l):
    d = 1
    for i in range(len(func)):
        if func[i] == 'R':
            d = -d
        else:
            if not l:
                return 'error'
            if d > 0:
                l.popleft()
            else:
                l.pop()
    
    rlt_lst = '['


    if l:
        if d > 0:
            l = list(l)
        else:
            l = list(l)[::-1]

        for i in range(len(l)):
            rlt_lst += l[i] + ','
        
        return rlt_lst[:len(rlt_lst) - 1] + ']'
    else:
        return rlt_lst + ']'

for _ in range(T):
    func = sys.stdin.readline().strip()
    n = int(input())
    nums = sys.stdin.readline().strip(',[]\n')
    lst = deque()

    nn = ''
    i = 0
    while i < len(nums):
        if '0' <= nums[i] <= '9':
            nn += nums[i]
            i += 1
        else:
            if nn:
                lst.append(nn)
            nn = ''
            i += 1
    if nn:
        lst.append(nn)

    rlt = ins(lst)

    print(rlt)
    