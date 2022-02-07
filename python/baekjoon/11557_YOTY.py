# Yangjojang of The Year
t = int(input())

for _ in range(t):
    school_num = int(input())
    school_lst = []
    m = -987654321
    yanjojang = None
    
    for __ in range(school_num):
        school_lst.append(list(input().split()))
    
    for i in school_lst:
        i[1] = int(i[1])
        if i[1] > m:
            m = i[1]
            yanjojang = i[0]
    
    print(yanjojang)

    