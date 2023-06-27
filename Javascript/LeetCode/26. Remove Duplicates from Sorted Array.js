/**
 * @param {number[]} nums
 * @return {number}
 */
var removeDuplicates = function(nums) {
  const numSet = new Set()
  const expectedNums = []

  // if num is in the set, it is not duplicates
  for (const num of nums) {
      if (!numSet.has(num)) {
          expectedNums.push(num)
          numSet.add(num)
      }
  }

  // change first k elements of nums to elements of expectedNums
  for (let i = 0; i < expectedNums.length; i += 1) {
      nums[i] = expectedNums[i]
  }

  return expectedNums.length
}