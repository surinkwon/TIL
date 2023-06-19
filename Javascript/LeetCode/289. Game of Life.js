/**
 * @param {number[][]} board
 * @return {void} Do not return anything, modify board in-place instead.
 */
var gameOfLife = function(board) {
  const m = board.length
  const n = board[0].length

  const newBoard = Array.from(new Array(m), v => new Array(n))
  const dr = [-1, -1, -1, 0, 0, 1, 1, 1]
  const dc = [-1, 0, 1, -1, 1, -1, 0, 1]

  for (let r = 0; r < m; r += 1) {
      for (let c = 0; c < n; c += 1) {
          let live = 0

          // count live cells
          for (let d = 0; d < dr.length; d += 1) {
              const [nr, nc] = [r + dr[d], c + dc[d]]

              if (0 <= nr && nr < m && 0 <= nc && nc < n) {
                  if (board[nr][nc]) {
                      live += 1
                  }
              }
          }

          // set cell's new condition
          if (live < 2) {
              newBoard[r][c] = 0
          } else if (live === 2) {
              newBoard[r][c] = board[r][c]
          } else if (live === 3) {
              newBoard[r][c] = 1
          } else {
              newBoard[r][c] = 0
          }
      }
  }

  // change old cell's condition to new condition
  for (let r = 0; r < m; r += 1) {
      for (let c = 0; c < n; c += 1) {
          board[r][c] = newBoard[r][c]
      }
  }
}