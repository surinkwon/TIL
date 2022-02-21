# 알파벳과 숫자를 동시에 접근하기 위한 dat
alph = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 0}
secret = list(input()) # 평문

k = input() # 암호 키

# 평문과 암호키를 함께 사용하기 위해 암호키를 평문 길이만큼 늘림
key = [0] * len(secret) 
i = j = 0
while i < len(secret):
    key[i] = k[j]
    i += 1
    j = (j + 1) % len(k)

# 암호 문자열(출력값)
secret_word = [0] * len(secret)

# 암호 문자열 리스트에 알파벳에 해당하는 숫자를 넣어줌
for letter in range(len(secret)):
    if secret[letter] != ' ':
        secret_word[letter] = (alph[secret[letter]] - alph[key[letter]]) % 26
    else:
        secret_word[letter] = ' '

# 해당 숫자를 다시 알파벳으로 변환
for num in range(len(secret_word)):
    for k, v in alph.items():
        if secret_word[num] == v:
            secret_word[num] = k

print(''.join(secret_word))