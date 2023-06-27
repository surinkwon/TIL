# [보석 쇼핑](https://school.programmers.co.kr/learn/courses/30/lessons/67258)

# 처음 생각한 풀이법

- 투포인터로 보석들을 차례대로 넣어가면서 모든 종류의 보석이 들었는지 확인하고 길이 비교
    - 보석의 종류를 담은 셋, 구매하는 보석의 종류를 담은 셋, 보석의 종류 당 몇 개를 구매하는지를 담은 객체 생성해서 풀이

# 틀렸다면 이후 풀이 방법 및 참고 자료

- 처음 짠 로직에서는 끝나는 인덱스가 gems의 길이와 같아지면 비교를 종료했다. 하지만 그 이후에도 더 길이가 짧은 리스트가 나올 수 있으므로 탐색을 더 진행해야 했다.
    - 처음 로직
        
        ```jsx
        while (e < gems.length) {
            if (buy.size !== gemTypeSet.size) {
                buy.add(gems[e])
                gemTypeObj[gems[e]] += 1
                e += 1
            } else {
                if (e - s < answer[1] - answer[0] + 1) {
                    answer[0] = s + 1
                    answer[1] = e
                }
                
                gemTypeObj[gems[s]] -= 1
                if (!gemTypeObj[gems[s]]) {
                    buy.delete(gems[s])
                }
                s += 1
            }
        }
        ```