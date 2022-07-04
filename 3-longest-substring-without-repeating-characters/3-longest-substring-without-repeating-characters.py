class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sub=""
        long={}
        if(len(s)==1):
            return 1
        for i in range(len(s)-1):
            sub=s[i]
            for j in range(i+1,len(s)):
                if s[j] in sub:
                    long[sub]=len(sub)
                    sub=""
                    break
                else:
                    sub = sub + s[j]
                    continue
            long[sub]=len(sub)
        long[sub]=len(sub)
        print(long)
        return max(long.values())
        