function solution(players, callings) {
  const place = {}
  
  for (let i = 0; i < players.length; i += 1) {
      place[players[i]] = i
  }
  
  for (const calling of callings) {
      const calledPlayerPlace = place[calling]
      const frontPlayer = players[calledPlayerPlace - 1]
      
      // players에서 등수 변환
      players[calledPlayerPlace] = frontPlayer
      players[calledPlayerPlace - 1] = calling
      
      // place에서 등수 변환
      place[calling] -= 1
      place[frontPlayer] += 1
  }
  
  return players;
}