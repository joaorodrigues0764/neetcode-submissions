class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        size_nums = len(nums)
        result = [1] * size_nums
        prefix = [1] * size_nums
        suffix = [1] * size_nums
        i = 1
        while i < size_nums:
            prefix[i] = prefix[i-1] * nums[i-1]
            i += 1
        for i in range(size_nums - 2, -1, -1):
            suffix[i] = suffix[i+1] * nums[i+1]
        i = 0
        while i < size_nums:
            result[i] = prefix[i] * suffix[i]
            i+=1
        return result














"""while i < len(nums):
            product = 1
            removed_num = nums.pop(i)
            for num in nums:
                product *= num
            result.append(product)
            nums.insert(i, removed_num)
            i += 1
        return result"""