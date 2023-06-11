function solution(n) {
    let answer = 0
    const colunm = new Array(n).fill(0)
    const rightDiagonal = new Array(n * 2 - 1).fill(0)
    const leftDiagonal = new Array(n * 2 - 1).fill(0)
    
    // n퀸 검사하는 함수
    function checkNQueen(r) {
        if (r === n) {
            answer += 1
        } else {
            for (let c = 0; c < n; c += 1) {
                
                // 해당 자리에 놓일 수 있으면 다음 열로 넘어감
                if (!colunm[c] && !rightDiagonal[r - c + n - 1] && !leftDiagonal[r + c]) {
                    colunm[c] = 1
                    rightDiagonal[r - c + n - 1] = 1
                    leftDiagonal[r + c] = 1
                    
                    checkNQueen(r + 1)
                    
                    colunm[c] = 0
                    rightDiagonal[r - c + n - 1] = 0
                    leftDiagonal[r + c] = 0
                }
            }
        }
    }
    
    checkNQueen(0)
    
    return answer
}