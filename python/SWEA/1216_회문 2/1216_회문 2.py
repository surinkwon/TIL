import sys

sys.stdin = open('input.txt')

T = 10

# 회문 판별 및 해당 회문 길이 반환 함수
def palindrome_len(lst):
    word = lst[::]
    while len(word) > 1:
        if word[0] == word[-1]:
            word = word[1:len(word) - 1]
        else:
            break

    if len(word) == 1 or len(word) == 0:
        return len(lst)
    elif len(word) > 1:
        return 0

# 전치 함수
def trans(lst):
    other_lst = [[0] * len(lst) for _ in range(len(lst))]
    for i in range(len(lst)):
        for j in range(len(lst)):
            other_lst[i][j] = lst[j][i]

    return other_lst


for tc in range(1, T + 1):
    test = int(input())
    # 글자 판을 받고 전치 행렬을 하나 만듦
    word_board = [list(input()) for _ in range(100)]
    word_cross_board = trans(word_board)
    max_pal = 0

    # 각 행렬에서 한 행씩 검사
    for k in range(len(word_board)): 
        for i in range(98):
            for j in range(i + 3, 100):
                pal = 0

                # 첫글자와 마지막 글자가 같으면 회문 검사 시작
                if word_board[k][j] == word_board[k][i]:
                    pal = palindrome_len(word_board[k][i:j+1])
                
                if word_cross_board[k][j] == word_cross_board[k][i]:
                    if pal < palindrome_len(word_cross_board[k][i:j+1]):
                        pal = palindrome_len(word_cross_board[k][i:j+1])

                # 회문 길이 최댓값 갱신
                if pal > max_pal:
                    max_pal = pal

    print(f'#{tc} {max_pal}')

