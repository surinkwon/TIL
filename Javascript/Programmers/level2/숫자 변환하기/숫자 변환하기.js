function makeXtoY(x, y, n) {
  const q = [x]
  const v = Array(y + 1).fill(0)
  v[x] = 1
  let total = q.length
  let curIndex = 0
  
  while (curIndex < total) {
      const cn = q[curIndex]
      
      if (cn === y) {
          return v[cn] - 1
      }
      
      // 3 곱하는 연산
      if (cn * 3 <= y && !v[cn * 3]) {
          q.push(cn * 3)
          v[cn * 3] = v[cn] + 1
          total += 1
      }
      
      // 2 곱하는 연산
      if (cn * 2 <= y && !v[cn * 2]) {
          q.push(cn * 2)
          v[cn * 2] = v[cn] + 1
          total += 1
      }
      
      // n 더하는 연산
      if (cn + n <= y && !v[cn + n]) {
          q.push(cn + n)
          v[cn + n] = v[cn] + 1
          total += 1
      } 
      
      curIndex += 1
  }
  
  return -1
}

function solution(x, y, n) {
  let answer = makeXtoY(x, y, n);
  return answer;
}