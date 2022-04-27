'''
조건 세 개만 만들어 놓으면 통과하지 못한 나머지는 남은 조건 하나 
'''
def whatKind():
    if lx2 < rx1 or hy1 > lowy2:
        return 'd'
    if (lx2 == rx1 and ly2 == ry1) or (lx2 == rx1 and ly1 == ry2):
        return 'c'
    if lx2 == rx1 and (ry1 <= ly1 <= ry2 or ry1 <= ly2 <= ry2 or ly1 <= ry1 <= ly2 or ly1 <= ry2 <= ly2):
        return 'b'
    if hy1 == lowy2 and (lowx1 <= hx1 <= lowx2 or lowx1 <= hx2 <= lowx2 or hx1 <= lowx1 <= hx2 or hx1 <= lowx2 <= hx2):
        return 'b'

    return 'a'



for _ in range(4):
    s1x1, s1y1, s1x2, s1y2, s2x1, s2y1, s2x2, s2y2 = map(int, input().split())
    if s1x2 <= s2x2:
        lx1, ly1, lx2, ly2 = s1x1, s1y1, s1x2, s1y2
        rx1, ry1, rx2, ry2 = s2x1, s2y1, s2x2, s2y2
    elif s2x2 <= s1x2:
        lx1, ly1, lx2, ly2 = s2x1, s2y1, s2x2, s2y2
        rx1, ry1, rx2, ry2 = s1x1, s1y1, s1x2, s1y2

    if s1y2 <= s2y2:
        hx1, hy1, hx2, hy2 = s2x1, s2y1, s2x2, s2y2
        lowx1, lowy1, lowx2, lowy2 = s1x1, s1y1, s1x2, s1y2
    elif s2y2 <= s1y2:
        hx1, hy1, hx2, hy2 = s1x1, s1y1, s1x2, s1y2
        lowx1, lowy1, lowx2, lowy2 = s2x1, s2y1, s2x2, s2y2


    rlt = whatKind()
    print(rlt)