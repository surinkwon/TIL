/**
 * 머리 찾는 함수
 * @param {string[]} board 쿠키가 놓인 판
 */
function findHead(board) {
  for (let r = 0; r < N; r += 1) {
    for (let c = 0; c < N; c += 1) {
      if (board[r][c] === '*') {
        return [r, c]
      }
    }
  }
}

/**
 * 길이 재는 함수
 * @param {number} sr 시작 행
 * @param {number} sc 시작 열
 * @param {number[]} dir 길이를 재는 방향
 * @returns 길이
 */
function calLength(sr, sc, dir) {
  let cnt = 1
  let [nr, nc] = [sr + dir[0], sc + dir[1]]

  while (nr >= 0 && N > nr && nc >= 0 && N > nc && board[nr][nc] === '*') {
    cnt += 1
    nr += dir[0] 
    nc += dir[1]
  }

  return cnt
}

// 입력
const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n')
const N = Number(input[0].trim())
const board = []
for (let i = 1; i < input.length; i += 1) {
  board.push(input[i].trim())
}

const head = findHead(board)
const heart = [head[0] + 1, head[1]]
const waist = calLength(heart[0] + 1, heart[1], [1, 0])
const leftArm = calLength(heart[0], heart[1] - 1, [0, -1])
const rightArm = calLength(heart[0], heart[1] + 1, [0, 1])
const leftLeg = calLength(heart[0] + waist + 1, heart[1] - 1, [1, 0])
const rightLeg = calLength(heart[0] + waist + 1, heart[1] + 1, [1, 0])

console.log(heart[0] + 1, heart[1] + 1)
console.log(leftArm, rightArm, waist, leftLeg, rightLeg);