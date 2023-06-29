/**
 * @param {number[]} nums
 * @return {number}
 */
var removeDuplicates = function(nums) {
  let cnt = 1           // duplicates count
  let curNum = nums[0]  // current number
  let j = 1

  for (let i = 1; i < nums.length; i += 1) {
      if (curNum === nums[i]) {
          // increase j until it appears less than three times
          if (cnt < 2) {
              nums[j] = nums[i]
              j += 1
              cnt += 1
          }
      } else {
          curNum = nums[i]
          cnt = 1
          nums[j] = nums[i]
          j += 1
      }
  }

  return j
}