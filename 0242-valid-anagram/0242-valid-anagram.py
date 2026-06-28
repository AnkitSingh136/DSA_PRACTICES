class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s1={}
        for i in range(len(s)):
            if s[i] in s1:
                s1[s[i]]+=1
            else:
                s1[s[i]]=1
        t1={}
        for i in range(len(t)):
            if t[i] in t1:
                t1[t[i]]+=1
            else:
                t1[t[i]]=1
        return True if s1==t1 else False




        