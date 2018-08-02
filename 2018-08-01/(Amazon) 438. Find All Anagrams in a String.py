class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        n = len(p)
        m = len(s)
        output = []
        shash = [0]*123
        phash = [0]*123
        if n > m:
            return output
        for i in p:
            phash[ord(i)] += 1
        for i in s[:n-1]:
            shash[ord(i)] += 1
            
        for i in range(n-1,m):
            shash[ord(s[i])] += 1
            if shash == phash:
                output.append(i-n+1)
            shash[ord(s[i-n+1])] -= 1   
            
        return output