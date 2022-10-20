/*
가장 많은 부서에 예산을 나눠주려 할 때 최대 몇 부서한테 나눠줄 수 있는지 구하는 문제
*/

function solution(d, budget) {
    
  d.sort((a, b) => {
      return a - b
  })
  
  let maxDepartment = 0
  
  for (i = 0; i < d.length; i += 1) {
      if (budget - d[i] < 0) {
          break
      } else {
          maxDepartment += 1
          budget -= d[i]
      }
  }
  
  return maxDepartment;
}