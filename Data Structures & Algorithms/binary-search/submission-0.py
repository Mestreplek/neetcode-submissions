class Solution:
    def search(self, nums: List[int], target: int) -> int:

        count = 0

        for num in nums:
            if num == target:
                return count
            count += 1
        
        return -1