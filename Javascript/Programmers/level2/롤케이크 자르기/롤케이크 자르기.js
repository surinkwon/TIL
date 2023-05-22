function solution(topping) {
    let answer = 0
    let totalToppingKind = 0
    const toppingIndex = {}
    
    // 토핑 종류 수와 각 토핑의 가장 마지막 인덱스 저장
    for (let i = 0; i < topping.length; i += 1) {
        if (toppingIndex[topping[i]] === undefined){
            totalToppingKind += 1
        }
        toppingIndex[topping[i]] = i
    }
    
    let olderBrothersTopping = new Set()
    let older = 0
    let younger = totalToppingKind
    
    // 잘라가면서 공평한지 확인
    for (let i = 0; i < topping.length - 1; i += 1) {
        // 형이 해당 토핑을 가지고 있는지 확인
        if (!olderBrothersTopping.has(topping[i])) {
            older += 1
            olderBrothersTopping.add(topping[i])
        }
        
        // 동생이 해당 토핑을 가지고있지 않은지 확인
        if (toppingIndex[topping[i]] <= i) {
            younger -= 1
        }
        
        if (older === younger) {
            answer += 1
        }
    }
    
    return answer
}