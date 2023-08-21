const input = require('fs').readFileSync('dev/stdin').toString()
const [N, K] = input.split('\n')[0].trim().split(' ').map(e => Number(e))
const place = input.split('\n')[1].trim().split('')
let totalTake = 0

for (let i = 0; i < N; i += 1) {
  if (place[i] === 'P') {
    // 앞쪽 살피기
    let take = false
    for (let j = K; j > 0; j -= 1) {
      if (i - j > -1 && place[i - j] === 'H') {
        take = true
        place[i - j] = ''
        totalTake += 1
        break
      }
    }

    // 뒷쪽 살피기
    if (!take) {
      for (let j = 1; j <= K; j += 1) {
        if (i + j < N && place[i + j] === 'H') {
          place[i + j] = ''
          totalTake += 1
          break
        } else if (i + j >= N) {
          break
        }
      }
    }
  }
}

console.log(totalTake);