function solution(edges) {
  const [START, DONUT, STICK, EIGHT] = [0, 1, 2, 3];
  const result = [0, 0, 0, 0];
  const inLine = {};
  const outLine = {};
  let maxEdge = 0;

  // 그래프 판별 함수
  function whatKindOfGragh(start) {
    if (!outLine[start]) {
      return STICK;
    }

    if (outLine[start].length > 1) {
      return EIGHT;
    }

    let current = outLine[start][0];

    while (current !== start) {
      // 더 이상 이어진 정점이 없으면 막대
      if (!outLine[current]) {
        return STICK;
      }

      // 중간에 간선이 두 개인 정점이 있으면 팔자
      if (outLine[current].length > 1) {
        return EIGHT;
      }

      current = outLine[current][0];
    }

    // 시작 정점으로 돌아왔으면 도넛
    return DONUT;
  }

  // 연결된 간선 정보 기록
  edges.forEach((lineData) => {
    const [from, to] = lineData;
    inLine[to] = true;
    outLine[from] ? outLine[from].push(to) : (outLine[from] = [to]);

    maxEdge = Math.max(from, to, maxEdge);
  });

  // 생성 정점 찾기
  for (let i = 1; i < maxEdge + 1; i += 1) {
    if (!inLine[i] && outLine[i] && outLine[i].length > 1) {
      result[START] = i;
      break;
    }
  }

  // 그래프 개수 세기
  outLine[result[START]].forEach((startEdge) => {
    const gragh = whatKindOfGragh(startEdge);
    result[gragh] += 1;
  });

  return result;
}
