def isSimilar(w_alph_num, w2) -> int:
    """ 두 단어가 비슷한 단어인지 검사하는 함수
    ----------
    Parameters
    ----------
    w_alph_num
        첫 단어의 알파벳 구성이 들어있는 배열
    w2
        두 번째 단어
    ----------
    Returns
    ----------
    비슷한 단어이면 1 아니면 0
    """
    if abs(len(words[0]) - len(w2)) > 1:
        return 0
    
    w2_alph_num = [0] * 26
    
    for i in range(len(w2)):
        w2_alph_num[ord(w2[i]) - ST] += 1
    
    dif_num = 0

    for i in range(len(w_alph_num)):
        dif_num += abs(w_alph_num[i] - w2_alph_num[i])
    
    if dif_num > 2:
        return 0

    return 1

N = int(input())

words = []

for _ in range(N):
    words.append(input())

w0_alph_num = [0] * 26
ST = ord('A')

for i in range(len(words[0])):
    w0_alph_num[ord(words[0][i]) - ST] += 1

rlt = 0

for i in range(1, N):
    rlt += isSimilar(w0_alph_num, words[i])

print(rlt)