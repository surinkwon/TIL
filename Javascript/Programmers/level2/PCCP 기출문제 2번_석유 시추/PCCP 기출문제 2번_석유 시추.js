function solution(land) {
  const dr = [0, 1, 0, -1];
  const dc = [1, 0, -1, 0];

  let maxOil = 0;
  let oilZoneNumber = 1;
  const oilZoneData = {};
  const v = Array.from(new Array(land.length), () => new Array(land[0].length));

  /**
   * bfs로 석유가 있는 공간을 확인하는 함수
   * @param {number} sr 시작하는 행
   * @param {number} sc 시작하는 열
   */
  function bfs(sr, sc) {
    const visitList = [[sr, sc]];
    const q = [[sr, sc]];
    let qr = 0;
    v[sr][sc] = 1;

    // 석유가 있는 자리 파악
    while (qr < q.length) {
      const [cr, cc] = q[qr];
      qr += 1;

      for (let d = 0; d < 4; d += 1) {
        const [nr, nc] = [cr + dr[d], cc + dc[d]];

        if (
          0 <= nr &&
          nr < land.length &&
          0 <= nc &&
          nc < land[0].length &&
          !v[nr][nc] &&
          land[nr][nc]
        ) {
          q.push([nr, nc]);
          v[nr][nc] = 1;
          visitList.push([nr, nc]);
        }
      }
    }

    // 해당 석유 자리에 얼마나 석유가 묻혀 있는지 기록
    oilZoneData[oilZoneNumber] = visitList.length;

    // 각 석유 자리가 어떤 번호인지 기록
    for (const visit of visitList) {
      const [r, c] = visit;
      v[r][c] = oilZoneNumber;
    }
  }

  // 첫 열부터 검색
  for (let c = 0; c < land[0].length; c += 1) {
    const includedOilZone = new Set();
    for (let r = 0; r < land.length; r += 1) {
      if (land[r][c] && !v[r][c]) {
        bfs(r, c);
        oilZoneNumber += 1;
      }

      if (v[r][c]) {
        includedOilZone.add(v[r][c]);
      }
    }

    let oilCount = 0;

    for (const oilZone of includedOilZone) {
      oilCount += oilZoneData[oilZone];
    }

    maxOil = Math.max(oilCount, maxOil);
  }

  return maxOil;
}
