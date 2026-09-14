from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff_map = {}
        for i, num in enumerate(nums):
            diff = target - num
            if(diff in  diff_map.keys()):
                return [i, diff_map[diff]]
            else:
                diff_map[num] = i

obj = Solution()
print(obj.twoSum([1, 2, 3, 4, 5, 6, 7, 8, 9], int(input("Target: "))))
