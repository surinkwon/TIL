// 밴할 수 있는지 판별하는 함수
function canBeBanned(user, banned) {
  if (user.length !== banned.length) {
    return false;
  }

  for (let i = 0; i < user.length; i += 1) {
    if (banned[i] !== "*" && user[i] !== banned[i]) {
      return false;
    }
  }

  return true;
}

function solution(user_id, banned_id) {
  const canBan = Array.from(new Array(banned_id.length), (v) => []);
  const answer = new Set();

  // 밴할 수 있는 아이디 판별
  for (
    let bannedIdIndex = 0;
    bannedIdIndex < banned_id.length;
    bannedIdIndex += 1
  ) {
    const bannedId = banned_id[bannedIdIndex];

    for (const userId of user_id) {
      if (canBeBanned(userId, bannedId)) {
        canBan[bannedIdIndex].push(userId);
      }
    }
  }

  // 밴 목록 뽑는 함수
  function pick(i, n, candidate) {
    if (i === n) {
      const candidateString = candidate
        .sort()
        .reduce((acc, cur) => acc + cur, "");
      answer.add(candidateString);
      return;
    }

    for (let j = 0; j < canBan[i].length; j += 1) {
      const id = canBan[i][j];
      if (!candidate.includes(id)) {
        pick(i + 1, n, [...candidate, id]);
      }
    }
  }

  // 밴 목록 뽑기
  pick(0, canBan.length, []);

  return answer.size;
}
