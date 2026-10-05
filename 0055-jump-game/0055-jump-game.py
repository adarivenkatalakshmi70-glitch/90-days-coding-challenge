class Solution:
    def canJump(self, nums: list[int]) -> bool:
        maxfind=0
        for i in range(len(nums)):
            if i>maxfind:
                return False
            maxfind=max(maxfind,i+nums[i])
        return True        