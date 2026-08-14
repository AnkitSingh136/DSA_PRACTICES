class Solution(object):
    def maximumLengthSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        h={}
        m=0
        left=0
        for i in range(len(s)):
            if s[i] not in h:
                h[s[i]]=1
            else:
                h[s[i]]+=1
            while(h[s[i]]>2):
                h[s[left]]-=1
                left+=1
            m=max(m,i-left+1)
        return m
            
        