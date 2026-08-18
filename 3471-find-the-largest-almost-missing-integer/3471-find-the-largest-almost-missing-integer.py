class Solution(object):
    def largestInteger(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        H=[]
        h1={}
        for i in range(len(nums)-k+1):
            h={}
            for j in range(i,i+k):
                if nums[j] not in h:
                    h[nums[j]]=1
                if nums[j] not in h1:
                    h1[nums[j]]=0
            H.append(h)
        
        for i in range(len(H)):
            a=H[i]
            for u,v in a.items():
                h1[u]+=1
        m=-1
        for u,v in h1.items():
            if v==1 and u>m:
                m=u

        return m

            

            
        