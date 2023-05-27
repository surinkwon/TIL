function solution(order) {
    let answer = 0
    let container = 1
    let secondaryContainer = []
    
    for (const curOrder of order) {
        // 실어야 하는 물건이 현재 컨테이너 벨트에서 꺼낼 수 있는 물건의 순서보다 크거나 같을 때
        if (curOrder >= container) {

            // 꺼내야 하는 물건 전의 물건들을 차례대로 보조 컨테이너 벨트로 옮김
            while (curOrder > container) {
                secondaryContainer.push(container)
                container += 1
            }

            // 물건을 트럭에 실음
            answer += 1
            container += 1
        } else {

            // 실어야 하는 물건이 컨테이너 벨트에서 꺼낼 수 있는 물건의 순서보다 작으면
            // 보조 컨테이너 벨트의 가장 앞 물건을 살펴보고 같으면 트럭에 싣고 다르면 정지
            if (secondaryContainer[secondaryContainer.length - 1] === curOrder) {
                answer += 1
                secondaryContainer.pop()
            } else {
                break
            }
        }
    }
    
    return answer
}