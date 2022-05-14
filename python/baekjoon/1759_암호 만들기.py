'''
브루트포스
'''

vowel = ['a', 'e', 'i', 'o', 'u']

def makePassword(i, n, password, length):
    global candidate

    if length == n:
        cnt = 0
        # 모음이 몇 개 있는지 체크
        for letter in range(len(password)):
            if password[letter] in vowel:
                cnt += 1
        
        # 모음이 한 개 이상, 자음이 두 개 이상이면 넣음
        if 0 < cnt < L - 1:
            candidate.append(password)
    
    elif i >= C:
        return

    else:
        # 이번 문자를 패스워드에 집어넣는 경우
        makePassword(i+1, n, password+alph[i], length+1)
        # 이번 문자를 패스워드에 집어넣지 않는 경우
        makePassword(i+1, n, password, length)


L, C = map(int, input().split())
alph = sorted(list(input().split()))
candidate = []

makePassword(0, L, '', 0)

for i in range(len(candidate)):
    print(candidate[i])