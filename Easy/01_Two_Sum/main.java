import java.util.HashMap;

class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> diff_Map = new HashMap<>();
        for(int i = 0; i < nums.length; i++){
           int diff = target - nums[i];
           if(diff_Map.containsKey(diff)){
            return new int[]{diff_Map.get(diff_Map), i};
           }
           else{
            diff_Map.put(nums[i], i);
           }
        }
        return new int[]{};
    }
}

public class main{
    public static void main(String[] args){
        int[] array = {1, 2, 3, 4, 5, 6, 7, 8, 9};
        Solution obj = new Solution();
        System.out.println(obj.twoSum(array, 13));
    }

    
}