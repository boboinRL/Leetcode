class Solution(object):
    def longestConsecutive(self, nums):
        #hashmap
        #set可以实现o(1)的查找，因为是找连续的数组，我只需要关心key在不在，而不需要知道value的值
        nums_set = set(nums)
        longest_length = {}
        for x in nums_set:
            if x - 1 not in nums_set:
                #record the beginning point position
                start_nums = x
                current_length = 1

                while start_nums + 1 in nums_set:
                    start_nums += 1
                    current_length += 1
                longest_length[x] = current_length
        return max(longest_length.values())     
