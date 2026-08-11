class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        L, maxF, res = 0, 0, 0
        count = {}

        for R in range(len(s)):
            count[s[R]] = 1 + count.get(s[R], 0)
            maxF = max(count[s[R]], maxF)

            while (R - L + 1) - maxF > k:
                count[s[L]] -= 1
                L += 1
            res = max(R -L +1 , res)
        return res
        