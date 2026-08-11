class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        maxRight = -1
        newMax = 0

        for i in range(len(arr)-1, -1, -1):
            newMax = max(newMax, arr[i])
            arr[i] = maxRight
            maxRight = newMax
        return arr