// 입력
let [N, cards, M, checkNumbers] = require('fs').readFileSync('./test.txt').toString().trim().split('\n')
cards = Array.from(cards.trim().split(' '), v => Number(v)).sort((a, b) => a - b)
checkNumbers = Array.from(checkNumbers.trim().split(' '), v => Number(v))

// 카드 찾는 함수
function doesHave(target) {
  let start = 0
  let end = cards.length
  
  while (start + 1 < end) {
    let mid = parseInt((start + end) / 2)

    if (cards[mid] === target) {
      return 1
    } else if (cards[mid] < target) {
      start = mid
    } else {
      end = mid
    }
  }

  // start나 end에 찾으려는 값이 있을 경우
  if (cards[start] === target || cards[end] === target) {
    return 1
  }

  return 0
}

const rlt = Array(M).fill(0)

// 각 카드를 가지고 있는지 검사
for (let i = 0; i < M; i += 1) {
  rlt[i] = doesHave(checkNumbers[i])
}

console.log(rlt.join(' '));