class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        result=[]
        h={}
        for i in range(len(nums1)):
            if nums1[i] not in h:
                h[nums1[i]]=1
        for i in range(len(nums2)):
            if nums2[i] in h and h[nums2[i]]>0:
                h[nums2[i]]-=1
                result.append(nums2[i])
        return result



        