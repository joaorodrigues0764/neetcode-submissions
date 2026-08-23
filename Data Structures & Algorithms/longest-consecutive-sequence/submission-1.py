class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        result = 0
        for num in nums_set:
            if (num - 1) in nums_set:
                continue
            
            len_seq = 1
            while (num + len_seq) in nums_set:
                    len_seq += 1
            
            if len_seq > result:
                result = len_seq
        
        return result

