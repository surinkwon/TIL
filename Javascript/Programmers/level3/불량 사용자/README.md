# [불량 사용자](https://school.programmers.co.kr/learn/courses/30/lessons/64064)

# 처음 생각한 풀이법

- 밴 아이디마다 가능한 아이디 수를 구하고 이를 곱하면 된다고 생각

# 틀렸다면 이후 풀이 방법 및 참고 자료

- 각 밴 아이디마다 일치하는 아이디가 중복될 수 있기 때문에 단순 곱셈으로는 풀 수 없었다. 중복되는 게 없도록 아이디를 뽑아야했는데 뽑는 순서 역시 중요하지 않으니 이전에 뽑은 리스트와 다른지도 비교해야했다. 따라서 재귀함수와 세트를 이용해서 탐색하며 풀이했다.
