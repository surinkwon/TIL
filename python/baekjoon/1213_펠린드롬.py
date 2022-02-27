def pal(word):
    odd = 0
    # 중복을 제외한 문자들
    l = []
    for i in word:
        if i not in l:
            l.append(i)

    l_cnt = [0] * len(l)
    for i in range(len(l_cnt)):
        l_cnt[i] = word.count(l[i])
        if l_cnt[i] % 2:
            odd += 1
            idx = i

    # 문자열 길이가 홀수일 때
    if len(word) % 2:
        # 홀수인 문자가 여러 개면 회문 못 만듦
        if odd > 1:
            return "I'm Sorry Hansoo"
        else:
            # 회문을 안에서부터 만들어나감
            name = l[idx]
            for i in range(len(l) - 1, -1, -1):
                if i != idx:
                    name = l[i] * (l_cnt[i] // 2) + name + l[i] * (l_cnt[i] // 2)
                else:
                    name = l[i] * (l_cnt[i] // 2) + name + l[i] * (l_cnt[i] // 2)
    
    # 문자열 길이가 짝수일 때
    else:
        # 홀수인 문자가 하나라도 있으면 회문 못 만듦
        if odd:
            return "I'm Sorry Hansoo"
        else:
            name = ''
            for i in range(len(l) - 1, -1, -1):
                name = l[i] * (l_cnt[i] // 2) + name + l[i] * (l_cnt[i] // 2)
    
    return name

# 사전 순서로 회문을 만들기위해 정렬함
letter = sorted(input())
rlt = pal(letter)

print(rlt)