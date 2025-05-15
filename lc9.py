class Solution:
    def isPalindrome(self, x):
        n=len(x)
        left=0
        right=n-1
        while left < right:
            if x[left]!=x[right]:
                return False
            left+=1
            right-=1
        return True 
if __name__ =="__main__":
    obj=Solution()
    # result1=obj.isPalindrome(["121"])
    result2=obj.isPalindrome(["-121"])
    # result3=obj.isPalindrome(["10"])
    # print("",result1)
    print("",result2)
    # print("",result3)                
        