class Solution:
    def isPalindrome(self, x:int) -> bool:
        x = str(x)
        return x == x[::-1]
        
  





obj = Solution()
print(obj.isPalindrome(int(input("Enter a Number: "))))