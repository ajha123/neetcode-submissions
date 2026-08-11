class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count, res = 0, 0

        for n in nums:
            if n == 0:
                res = max(count, res)
                count = 0
            else:
                count += 1
        return max(count, res)
        