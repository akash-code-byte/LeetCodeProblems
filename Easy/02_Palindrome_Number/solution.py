class Solution:
    def isPalindrome(self, x:int) -> bool:
        var, rev = x, 0
        
        while(var != 0):
            rev = rev * 10 + var % 10
            var = var // 10
            if(var == 0):
                rev = rev * 10
        return x == rev
        
  





obj = Solution()
print(obj.isPalindrome(int(input("Enter a Number: "))))