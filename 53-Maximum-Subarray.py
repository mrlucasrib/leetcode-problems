class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        currSum = 0
        for n in  nums:
            if currSum < 0:
                currSum = 0
            currSum += n
            if maxSum < currSum:
                maxSum = currSum
        return maxSum
