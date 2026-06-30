class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        h={}
        for i in range(len(nums)):
            if nums[i] not in h:
                h[nums[i]]=0
            h[nums[i]]+=1
        result=[]
        sorted_h=sorted(h.items(), key=lambda x: x[1], reverse=True)
        print(sorted_h)
        for key,value in sorted_h:
            result.append(key)
            if len(result)==k:
                break
        return result





        