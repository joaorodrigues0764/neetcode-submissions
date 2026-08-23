class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict_nums = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in dict_nums:
                return [dict_nums[complement],i]
            else:
                dict_nums[num] = i
        