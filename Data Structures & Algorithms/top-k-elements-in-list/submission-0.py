class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_dict = {}
        result = []
        for num in nums:
            if num in nums_dict:
                nums_dict[num] += 1
            else:
                nums_dict[num] = 1
        for i in range(k):
            big_value = max(nums_dict.values())
            for key, value in nums_dict.items():
                if value == big_value:
                    key_del = key
                    break
            result += [key_del]
            del nums_dict[key_del]
        return result

