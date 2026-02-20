class Solution(object):
    def twoSum(self, nums, target):
         #directly use hashmap
        hashmap = {}
        #directly use enumerate 遍历数据
        for i, x in enumerate (nums): # it will return both index and number
            y = target - x

            if y in hashmap:
                return [i, hashmap[y]]
            hashmap[x] = i
        