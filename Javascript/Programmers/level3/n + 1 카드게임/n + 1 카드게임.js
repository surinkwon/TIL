function solution(coin, cards) {
  const TARGET = cards.length + 1;
  let round = 1;
  const canMake = [[], [], []];
  let zeroCoinMakingIndex = 0;
  let oneCoinMakingIndex = 0;
  let twoCoinMakingIndex = 0;
  const notUse = new Set();
  const needCoin = new Array(cards.length + 1).fill(1);

  // 처음 받는 카드 처리
  for (let i = 0; i < cards.length / 3; i += 1) {
    const card = cards[i];
    needCoin[card] = 0;

    if (notUse.has(TARGET - card)) {
      const neededCoin = needCoin[card] + needCoin[TARGET - card];
      canMake[neededCoin].push(card);
    }

    notUse.add(card);
  }

  // 라운드 진행
  for (let i = parseInt(cards.length / 3); i < cards.length; i += 2) {
    // 각 카드마다 처리
    for (let j = 0; j < 2; j += 1) {
      const card = cards[i + j];

      if (notUse.has(TARGET - card)) {
        const neededCoin = needCoin[card] + needCoin[TARGET - card];
        canMake[neededCoin].push(card);
      }

      notUse.add(card);
    }

    // 라운드 마무리
    // 낼 카드가 없으면 종료
    if (
      !(canMake[0].length - zeroCoinMakingIndex) &&
      !(canMake[1].length - oneCoinMakingIndex) &&
      !(canMake[2].length - twoCoinMakingIndex)
    ) {
      break;
    }

    // 낼 카드가 있으면
    let card1;
    if (canMake[0].length - zeroCoinMakingIndex) {
      card1 = canMake[0][zeroCoinMakingIndex];
      zeroCoinMakingIndex += 1;
    } else if (canMake[1].length - oneCoinMakingIndex) {
      card1 = canMake[1][oneCoinMakingIndex];
      coin -= 1;
      oneCoinMakingIndex += 1;
    } else {
      card1 = canMake[2][twoCoinMakingIndex];
      coin -= 2;
      twoCoinMakingIndex += 1;
    }
    const card2 = TARGET - card1;

    notUse.delete(card1);
    notUse.delete(card2);

    // 카드를 낼 수 있어도 코인을 초과해서 썼다면 라운드 종료
    if (coin < 0) {
      break;
    }

    round += 1;
  }

  return round;
}

const result = solution(4, [3, 6, 7, 2, 1, 10, 5, 9, 8, 12, 11, 4]);
