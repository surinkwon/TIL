function solution(gems) {
    var answer = [-1, gems.length]
    const gemTypeSet = new Set()
    const gemTypeObj = {}
    const buy = new Set()
    
    // 타입 저장
    for (const gem of gems) {
        gemTypeSet.add(gem)
        gemTypeObj[gem] = 0
    }
    
    let [s, e] = [0, 0]
    
    while (true) {
        // 모든 종류의 보석이 포함되어 있지 않다면 다음 보석 구매
        if (buy.size !== gemTypeSet.size) {

            // 더 구매할 보석이 없으면 종료
            if (e === gems.length) {
                break
            }

            buy.add(gems[e])
            gemTypeObj[gems[e]] += 1
            e += 1
        } else {

            // 모든 종류의 보석이 포함돼 있으면 길이 비교
            if (e - s < answer[1] - answer[0] + 1) {
                answer[0] = s + 1
                answer[1] = e
            }
            
            // 가장 처음 샀던 보석 제외
            gemTypeObj[gems[s]] -= 1
            if (!gemTypeObj[gems[s]]) {
                buy.delete(gems[s])
            }
            s += 1
        }
    }
    
    return answer
}