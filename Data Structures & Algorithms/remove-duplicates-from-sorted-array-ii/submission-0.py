class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        L = 0

        for num in nums:
            if L < 2 or nums[L-2] != num:
                nums[L] = num
                L += 1
          
        return L
        