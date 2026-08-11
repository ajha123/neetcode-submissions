# The "Bucket Sort" Strategy for Top K Frequent
# Count Map: Use a HashMap (Dictionary) to get {number: frequency}.

# Empty Buckets: Initialize a list of empty lists [[] for i in range(len(nums) + 1)].

# Fill Buckets: Iterate through the map and use the count as the index to append the number: freq[cnt].append(num).

# Reverse Iterate: Loop through the buckets from len(freq) - 1 down to 1.

# Flatten & Limit: Use a nested loop to pull numbers out of the buckets into res. Return immediately once len(res) == k.
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums)+1)]

        for num in nums:
            count[num] = 1 + count.get(num, 0)
        for num, cnt in count.items():
            # freq = [[],[3],[2],[1],[],[],[]]
            freq[cnt].append(num) 
        
        res = []
        for i in range(len(freq) -1 , 0 , -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res
        