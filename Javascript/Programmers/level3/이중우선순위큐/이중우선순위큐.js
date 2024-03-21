function solution(operations) {
  const numberSet = new Set();
  const numberMap = new Map();
  let maxNum, minNum;

  for (let i = 0; i < operations.length; i += 1) {
    let [op, num] = operations[i].split(" ");
    num = parseInt(num);

    if (op === "I") {
      numberSet.add(num);
      numberMap.has(num) ? (numberMap[num] += 1) : numberMap.set(num, 1);
      if (!maxNum || num > maxNum) {
        maxNum = num;
      }

      if (!minNum || num < minNum) {
        minNum = num;
      }
    } else {
      if (!numberSet.size) {
        continue;
      }

      if (num === -1) {
        numberMap.set(minNum, numberMap.get(minNum) - 1);
        if (!numberMap.get(minNum)) {
          numberSet.delete(minNum);
        }
      } else {
        numberMap.set(maxNum, numberMap.get(maxNum) - 1);
        if (!numberMap.get(maxNum)) {
          numberSet.delete(maxNum);
        }
      }

      minNum = numberSet.size ? Math.min(...numberSet) : undefined;
      maxNum = numberSet.size ? Math.max(...numberSet) : undefined;
    }
  }

  if (numberSet.size === 0) {
    return [0, 0];
  }

  return [maxNum, minNum];
}

const result = solution([
  "I 16",
  "I -5643",
  "D -1",
  "D 1",
  "D 1",
  "I 123",
  "D -1",
]);
