class Solution(object):
    def singleNumber(self, nums):
        num_count = {}
        for num in nums:
            if num in num_count:
                num_count[num] += 1
            else:
                num_count[num] = 1
        for key, value in num_count.items():
            if value == 1:
                return key