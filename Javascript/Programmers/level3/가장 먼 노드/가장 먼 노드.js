function bfs(start, vertex) {
  const v = new Array(vertex.length);
  const q = [start];

  // 초기화
  let qf = 0;
  v[start] = 1;

  while (q.length > qf) {
    const cn = q[qf];
    qf += 1;

    for (let d = 0; d < vertex[cn].length; d += 1) {
      const nn = vertex[cn][d];
      if (!v[nn]) {
        q.push(nn);
        v[nn] = v[cn] + 1;
      }
    }
  }

  return v;
}

function getFarNodeNumber(visit) {
  let farNode = 0;
  let maxDistance = visit[0];

  visit.sort((a, b) => b - a);

  for (let i = 0; i < visit.length; i += 1) {
    if (visit[i] !== maxDistance) {
      break;
    }

    farNode += 1;
  }

  return farNode;
}

function solution(n, edge) {
  const vertex = Array.from(new Array(n + 1), () => []);

  for (let i = 0; i < edge.length; i += 1) {
    const [v1, v2] = edge[i];
    vertex[v1].push(v2);
    vertex[v2].push(v1);
  }

  const visit = bfs(1, vertex);

  return getFarNodeNumber(visit);
}
