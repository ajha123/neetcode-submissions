class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        curSum = 0
        # maxL, maxR = 0, 0
        # L = 0

        for R in nums:
            if curSum < 0:
                curSum = 0
               
            curSum += R
            maxSum = max(maxSum, curSum)
        return maxSum
            


        