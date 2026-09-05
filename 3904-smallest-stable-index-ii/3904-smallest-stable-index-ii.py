class Solution(object):
    def firstStableIndex(self, nums, k):
        arr=[]
        m1=nums[-1]
        for i in range(len(nums)-1,-1,-1):
            m1=min(m1,nums[i])
            arr.append(m1)
        arr.reverse()
        m2=nums[0]

        for j in range(len(nums)):
            m2=max(m2,nums[j])
            if m2-arr[j] <=k:
                return j
        return -1
        