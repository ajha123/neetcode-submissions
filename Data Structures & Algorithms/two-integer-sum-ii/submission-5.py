class Solution:
    #Two Pointer
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        L, R = 0, len(numbers) - 1

        while L < R:
            if numbers[L] + numbers[R] > target:
                R -= 1
            elif numbers[L] + numbers[R] < target:
                L += 1
            else:
                return [L+1,R+1]
        return []

        
    # # HashMap
    # def twoSumHashMap(self, numbers: List[int], target: int) -> List[int]:
    #     mp = defaultdict(int)
    #     for i in range len(numbers):
    #         temp = target - numbers[i]
    #         if mp[temp]:
    #             return [mp[temp], i+1]
    #         mp[numbers[i]] = i+1
    #     return[]

    

        