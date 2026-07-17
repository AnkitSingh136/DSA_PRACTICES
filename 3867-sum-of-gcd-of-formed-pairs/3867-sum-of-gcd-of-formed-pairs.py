class Solution(object):
    def gcdSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m=nums[0]
        arr=[]
        for i in range(len(nums)):
            m=max(m,nums[i])
            mx=m
            while mx!=0:
                temp=mx
                mx=nums[i]%mx
                nums[i]=temp
            arr.append(nums[i])
        arr.sort()
        s=0
        i=0
        j=len(arr)-1
        while(i<j):
            a=arr[i]
            b=arr[j]
            while b!=0:
                temp=b
                b=a%b
                a=temp
            i=i+1
            j=j-1
            s+=a

        return s




        