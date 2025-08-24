from typing import List
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left = 0
        zero_count = 0
        max_len = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                zero_count += 1

            while zero_count > 1:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1

            # We must delete one element, so subtract 1 from window size
            max_len = max(max_len, right - left)

        return max_len
sol=Solution()
nums=[1,1,0,1]
print(sol.longestSubarray(nums))  #output=3