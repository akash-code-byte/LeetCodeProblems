from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = 0
        diff_map = dict({})
        for i in range(len(nums)):
            diff = target - nums[i]
            if(diff in  diff_map.keys()):
                return [i, diff_map[diff]]
            else:
                diff_map[nums[i]] = i




        









obj = Solution()
print(obj.twoSum([1, 2, 3, 4, 5, 6, 7, 8, 9], int(input("Target: "))))
