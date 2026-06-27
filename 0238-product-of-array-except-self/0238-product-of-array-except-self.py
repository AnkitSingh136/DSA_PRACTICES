class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
       
        prefix_p=[1]
        pp=1
        sufix_p=[1]
        sp=1
        for i in range(len(nums)-1):
            pp*=nums[i]
            prefix_p.append(pp)
        for i in range(len(nums)-1,0,-1):
            sp*=nums[i]
            sufix_p.append(sp)
        sufix_p.reverse()
        result=[]
        for i in range(len(nums)):
            result.append(prefix_p[i]*sufix_p[i])
        return result

        









        