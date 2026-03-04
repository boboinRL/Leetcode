class Solution(object):
    def topKFrequent(self, nums, k):
        # similar to longest consecutive sequence
        # 1. 统计频率
        num_set = set(nums)
        count = {}
        for n in nums:
            # 这里怎么写能把 n 的次数加进 count 里？
            count[n] = count.get(n,0)+1
            
        # 2. 创建桶 (频率作为索引)
        # 桶的大小应该是 len(nums) + 1
        freq = [[] for _ in range(len(nums) + 1)] #就创建这么多个空列表
        
        # 3. 把 count 里的数据填进桶里，这里有转变了一下，频率为索引，数字为key
        for n, c in count.items():
            freq[c].append(n)
            
        # 4. 准备结果
        res = []
        # 倒着遍历桶，取前 k 个数字
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]: # 如果这个抽屉里有数字
                res.append(num)
                if len(res) == k: # 只要凑够 k 个，立刻收工
                    return res