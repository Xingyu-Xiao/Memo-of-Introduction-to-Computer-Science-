from typing import List
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        import bisect
        set_nums = set(nums)
        if target in set_nums:
            return [bisect.bisect_left(nums, target), bisect.bisect_right(nums, target)-1]
        else:
            return [-1, -1]
