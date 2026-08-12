class Solution(object):
    def missingInteger(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start=0
        length=0
        maxi=0
        s=nums[0]
        for i in range(1,len(nums)):
            if nums[i]==nums[i-1]+1:
                s+=nums[i]
            else:
                for i in range(s,s+51):
                    if i not in nums:
                        return i
                
        return sum(nums) if len(nums)>1 else sum(nums)+1





        