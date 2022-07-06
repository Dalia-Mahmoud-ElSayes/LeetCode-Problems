class Solution:
    def romanToInt(self, s: str) -> int:
        dict={"I":1 ,"V":5 ,"X":10 , "L":50 , "C":100 , "D":500 , "M":1000}
        i=0
        num=0
        while i < len(s):
            if i==len(s)-1:
                num=num+dict[s[i]]
                break
            elif (dict[s[i]]< dict[s[i+1]]):
                num=num+(dict[s[i+1]]-dict[s[i]])
                i=i+1
            else:
                num=num+dict[s[i]]
            i=i+1
            
        return num
            