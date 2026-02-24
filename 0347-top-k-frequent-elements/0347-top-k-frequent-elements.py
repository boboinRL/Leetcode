class Solution(object):
    def topKFrequent(self, nums, k):
        # 1. 统计频率：数字 -> 出现次数
        # 这一步是 O(n)
        count = {}
        for n in nums:
            count[n] = 1 + count.get(n, 0)

        # 2. 桶排序：出现次数 -> [数字列表]
        # 桶的长度设为 len(nums) + 1，因为一个数最多出现 len(nums) 次
        # 这一步也是 O(n)
        freq = [[] for _ in range(len(nums) + 1)]
        for n, c in count.items():
            freq[c].append(n)

        # 3. 倒着遍历桶，收集前 k 个高频元素
        # 我们用到了刚才讨论的 range(start, stop, step) 逆序写法
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                # 一旦收集够了 k 个，立刻返回
                if len(res) == k:
                    return res