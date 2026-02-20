import numpy as np
class Solution(object):
    def productExceptSelf(self, nums):
        n = len(nums)
        res = [1] * n #快捷初始化列表，里面装上n个1

        # 1. 第一遍：计算每个元素左边的乘积
        # 比如 [1, 2, 3, 4] -> res 变成 [1, 1, 1*2, 1*2*3]
        prefix = 1
        for i in range(n):
            res[i] = prefix #这里思路和我不一样，这里是把乘积给到res[i]. 这里在i=0的时候，就已经把1给到res[0]当中了
            prefix *= nums[i] # 先存后乘
            
        # 2. 第二遍：乘以每个元素右边的乘积
        # 倒着走，把右边的乘积动态地乘进去
        suffix = 1
        for i in range(n - 1, -1, -1):
            res[i] *= suffix
            suffix *= nums[i]
            
        return res

        