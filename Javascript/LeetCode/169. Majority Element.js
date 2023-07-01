/**
 * @param {number[]} nums
 * @return {number}
 */
var majorityElement = function(nums) {
  const obj = {}

  for (const num of nums) {
      // if num already apears
      if (obj[num]) {
          obj[num] += 1
          if (obj[num] >= nums.length / 2) {
              return num
          }
      } 
      
      // if num apears for the first time
      else {
          obj[num] = 1
      }
  }

  // if the length of nums is 1
  return nums[0]
}