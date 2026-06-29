class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        h={}
        result=[]
        for i in range(len(strs)):
            key=''.join(sorted(strs[i]))
            if key not in h:
                h[key]=[]
            if key in h:
                h[key].append(strs[i])
        result=[]
        for key,value in h.items():
            result.append(h[key])
        return result
            

    



        