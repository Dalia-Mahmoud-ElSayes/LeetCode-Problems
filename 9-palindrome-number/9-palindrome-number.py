class Solution:
    def isPalindrome(self, x: int) -> bool:
        num=str(x)
        if(num[0]=='-'):
            return False
        else:
            for i in range(0,(len(num)//2)):
                if(num[i]==num[-1-i]):
                    continue
                else:
                    return False
            return True
        