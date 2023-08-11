let [str1, str2] = require('fs').readFileSync('./test.txt').toString().split('\n')
str1 = str1.trim()
str2 = str2.trim()

const DP = Array.from(new Array(str1.length), () => new Array(str2.length))

// 첫 행 채우기
DP[0][0] = str1[0] === str2[0] ? 1 : 0

for (let c = 1; c < str2.length; c += 1) {
  DP[0][c] = str1[0] === str2[c] ? 1 : Math.max(0, DP[0][c - 1])
}

// 첫 열 채우기
for (let r = 1; r < str1.length; r += 1) {
  DP[r][0] = str1[r] === str2[0] ? 1 : Math.max(0, DP[r - 1][0])
}

// 최장 길이 구하기
for (let r = 1; r < str1.length; r += 1) {
  for (let c = 1; c < str2.length; c += 1) {
    DP[r][c] = str1[r] === str2[c] ? DP[r - 1][c - 1] + 1 : Math.max(DP[r - 1][c], DP[r][c - 1])
  }
}

console.log(DP[str1.length - 1][str2.length - 1])