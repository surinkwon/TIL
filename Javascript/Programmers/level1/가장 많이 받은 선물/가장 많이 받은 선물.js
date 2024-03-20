function solution(friends, gifts) {
  const friendsNum = friends.length;
  const giveAndTake = Array.from(new Array(friendsNum), (v) =>
    new Array(friendsNum).fill(0)
  );
  const giftIndices = new Array(friendsNum).fill(0);
  const friendsIndex = {};
  const nextMonthTakeNumber = new Array(friendsNum).fill(0);

  // 친구 인덱스 기록
  friends.forEach((friend, index) => {
    friendsIndex[friend] = index;
  });

  // 주고 받은 내역 기록 및 선물 지수 계산
  gifts.forEach((giftData) => {
    const [giver, taker] = giftData.split(" ");
    const giverIndex = friendsIndex[giver];
    const takerIndex = friendsIndex[taker];

    giveAndTake[giverIndex][takerIndex] += 1;
    giftIndices[giverIndex] += 1;
    giftIndices[takerIndex] -= 1;
  });

  // 다음 달 선물 예측
  for (let a = 0; a < friendsNum; a += 1) {
    for (let b = a + 1; b < friendsNum; b += 1) {
      const aTobGiveNum = giveAndTake[a][b];
      const bToaGiveNum = giveAndTake[b][a];

      // a가 b보다 많이 줬을 때
      if (aTobGiveNum > bToaGiveNum) {
        nextMonthTakeNumber[a] += 1;
      }
      // b가 a보다 많이 줬을 때
      else if (aTobGiveNum < bToaGiveNum) {
        nextMonthTakeNumber[b] += 1;
      }
      // 둘 다 동일하게 주고 받았을 때
      else {
        // 선물 지수가 높은 사람이 선물을 받음
        if (giftIndices[a] > giftIndices[b]) {
          nextMonthTakeNumber[a] += 1;
        } else if (giftIndices[a] < giftIndices[b]) {
          nextMonthTakeNumber[b] += 1;
        }
      }
    }
  }

  return Math.max(...nextMonthTakeNumber);
}
