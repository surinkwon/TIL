/**
 * 최소 이동 횟수 찾는 함수
 * @param {string[][]} board 
 * @param {number[]} start 
 * @param {number[]} goal 
 * @returns number
 */
function findWay(board, start, goal) {
    const dr = [0, 1, 0, -1]
    const dc = [1, 0, -1, 0]
    const q = [start]
    let f = 0
    const v = Array.from(new Array(board.length), v => new Array(board[0].length).fill(0))
    v[start[0]][start[1]] = 1
    
    while (f < q.length) {
        const [cr, cc] = q[f]
        f += 1
        
        if (cr === goal[0] && cc === goal[1]) {
            return v[cr][cc] - 1
        }
        
        for (let d = 0; d < dr.length; d += 1) {
            let [nr, nc] = [cr, cc]
            
            // 장애물이나 벽에 닿을 때까지 이동
            while (0 <= nr + dr[d] && board.length > nr + dr[d] && 0 <= nc + dc[d] && board[0].length > nc + dc[d] && board[nr+dr[d]][nc+dc[d]] !== 'D') {
                nr += dr[d]
                nc += dc[d]
            }
            
            if (!v[nr][nc]) {
                q.push([nr, nc])
                v[nr][nc] = v[cr][cc] + 1
            }
        }
    }
    
    return -1
}

function solution(board) {
    const start = [0, 0]
    const goal = [0, 0]
    
    // 시작 위치, 목표 위치 찾기
    for (let r = 0; r < board.length; r += 1) {
        for (let c = 0; c < board[0].length; c += 1) {
            if (board[r][c] === 'R') {
                [start[0], start[1]] = [r, c]
            } else if (board[r][c] === 'G') {
                [goal[0], goal[1]] = [r, c]
            }
        }
    }
    
    const answer = findWay(board, start, goal)
    return answer
}