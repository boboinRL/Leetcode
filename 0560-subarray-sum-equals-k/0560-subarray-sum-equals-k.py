class Solution(object):
    def subarraySum(self, nums, k):
        # count 用于记录满足条件的子数组数量
        count = 0
        # cur_sum 用于记录当前遍历到的前缀和
        cur_sum = 0
        # prefix_sums 哈希表用于存储前缀和出现的次数
        # 初始化 {0: 1} 是为了处理当前缀和正好等于 k 的情况
        prefix_sums = {0: 1}
        
        for num in nums:
            cur_sum += num  # 更新当前前缀和
            
            # 检查 cur_sum - k 是否在之前的记录中
            # 如果在，说明从那个点到当前点的子数组和为 k
            if (cur_sum - k) in prefix_sums:
                count += prefix_sums[cur_sum - k]
            
            # 将当前前缀和存入哈希表，如果已存在则次数 +1
            prefix_sums[cur_sum] = prefix_sums.get(cur_sum, 0) + 1
            
        return count
        