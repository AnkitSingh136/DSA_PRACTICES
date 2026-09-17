class Solution(object):
    def countSpecialIntegers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        h={}
        
        for i in range(len(nums)):
            if nums[i] not in h:
                h[nums[i]]=[]
            h[nums[i]].append(i)
        result=[]
        for u,v in h.items():
            print(u,v)
            if len(v)==3 and v[1]-v[0]==v[2]-v[1]:
                result.append(u)



        return len(result)

        