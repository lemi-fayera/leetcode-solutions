/**
 * @param {number[]} nums
 * @return {number}
 */
var sumOfUnique = function(nums) {
    let right = []
    let total = 0
    for(let i = 0; i < nums.length; i++) {
        let left = nums.slice(i+1)

        if(!left.includes(nums[i]) && !right.includes(nums[i])){
            total += nums[i]
        }
        right.push(nums[i])

    }
    return total

};