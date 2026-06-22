class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums[:]=sorted(set(nums))
        print(nums) 
        m=0
        count=1
        if len(nums)==0:
            return 0
        if len(nums)==1:
            return 1
        for i in range(1,len(nums)):
            if nums[i]==nums[i-1]+1:
                count+=1
                m=max(count,m)
            else:
                count=1
                m=max(count,m)
        return m






        