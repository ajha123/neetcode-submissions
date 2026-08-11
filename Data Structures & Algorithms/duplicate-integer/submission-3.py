class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_hash = {}

        for n in nums:
            if n in nums_hash:
                return True
            nums_hash[n] = 1
        return False
