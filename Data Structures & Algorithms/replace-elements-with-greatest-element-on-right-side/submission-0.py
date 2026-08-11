class Solution:
    # def replaceElements(self, arr: List[int]) -> List[int]:
        # ans = [0] * len(arr)
        # for i in range(len(arr)):
        #     rightMax = - 1
        #     for j in range(i+1, len(arr)):
        #         rightMax = max(rightMax, arr[j])
        #     ans[i] = rightMax
        # return ans
    
    def replaceElements(self, arr: List[int]) -> List[int]:
        rightMax = - 1
        newMax = 0
        for i in range(len(arr)-1, -1, -1):
            newMax = max(newMax, arr[i])
            arr[i] = rightMax
            rightMax = newMax
        return arr