class Solution:

    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        curSum = 0
        maxL, maxR = 0, 0
        L = 0

        for R in range(len(nums)): 
              # ✅ iterate with index
            if curSum < 0:
                curSum = 0
                L = R                # ✅ reset start index

            curSum += nums[R]

            if curSum > maxSum:
                maxSum = curSum
                maxL, maxR = L, R 
        print("Best subarray:", nums[maxL:maxR+1])  # optional
        return maxSum

        
    

    # for R in range(len(nums)):   # ✅ iterate with index
    #     if curSum < 0:
    #         curSum = 0
    #         L = R                # ✅ reset start index

    #     curSum += nums[R]

    #     if curSum > maxSum:
    #         maxSum = curSum
    #         maxL, maxR = L, R    # ✅ track best indices

    # print("Best subarray:", nums[maxL:maxR+1])  # optional
    # return maxSum
    # def maxSubArray(self, nums: List[int]) -> int:
    #     maxSum = nums[0]
    #     curSum = 0
    #     # maxL, maxR = 0, 0
    #     # L = 0

    #     for R in nums:
    #         if curSum < 0:
    #             curSum = 0
               
    #         curSum += R
    #         maxSum = max(maxSum, curSum)
    #     return maxSum
            


        