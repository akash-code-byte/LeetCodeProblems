import java.util.Scanner;

class Solution{
    public boolean isPalindrome(int x){
        int var = x,rev = 0;
        while (var != 0) {
            rev = rev * 10 + var % 10;
            var = var / 10;
            if(var == 0){
               rev = rev * 10;
            }
        }
        return x == rev;
        
    }
}

public class Main{
    public static void main(String[] args){
        Solution obj = new Solution();
        Scanner input = new Scanner(System.in);
        System.out.println("Enter a NUmber: ");
        System.out.println(obj.isPalindrome(input.nextInt()));
        input.close();
    }
}