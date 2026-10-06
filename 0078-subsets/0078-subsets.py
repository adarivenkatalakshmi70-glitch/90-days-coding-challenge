class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        n=len(nums)
        subset=1<<n
        ans=[]
        for i in range(subset):
            lst=[]
            for j in range(n):
                if i&(1<<j):
                    lst.append(nums[j])
            ans.append(lst)
        return ans            
         
        