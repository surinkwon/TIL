/*JS에는 Python에서 Tuple같은 게 없어서 Set에 (1, 2) 이런 형식으로 집어넣을 수 없다.
  저렇게 집어 넣으면 마지막 원소만 Set에 들어간다.
  리스트를 집어 넣으면 리스트가 들어가지만 has 메서드로 검사가 안 된다. 같은 리스트 찾아도 false가 반환된다.
  따라서 문자열로 만들어서 추가했다.
*/


function solution(dirs) {
  let answer = 0;
  const curCoord = [0, 0]
  const orders = {'U': [0, 1], 'D': [0, -1], 'R': [1, 0], 'L': [-1, 0]}
  const path = new Set()
  
  for (const order of dirs) {
      const [cx, cy] = curCoord
      const [dx, dy] = orders[order]
      
      const [nx, ny] = [cx + dx, cy + dy]
      
      if (Math.abs(nx) <= 5 && Math.abs(ny) <= 5) {
          if (!path.has(`${cx}${cy}${nx}${ny}`) && !path.has(`${nx}${ny}${cx}${cy}`)) {
              answer += 1
              path.add(`${cx}${cy}${nx}${ny}`)
          }
          curCoord[0] = nx
          curCoord[1] = ny
      }
  }
  
  return answer;
}