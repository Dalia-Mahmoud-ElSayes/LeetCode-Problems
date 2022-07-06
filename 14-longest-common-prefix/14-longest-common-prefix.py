class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_length=len(min(strs, key=len))
        i=0
        common=""
        while i< min_length:
            for j in range(0,len(strs)-1):
                if strs[j][i]==strs[j+1][i]:
                    continue
                else:
                    return common
                
            common=common+strs[0][i]
            i=i+1
        return common