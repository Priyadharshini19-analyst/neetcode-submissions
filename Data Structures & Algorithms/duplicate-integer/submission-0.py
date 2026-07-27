class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for x in nums:
            if x in seen:      # O(1) — have I seen this before?
                return True
            seen.add(x)
        return False
        