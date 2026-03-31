class Solution(object):
    def characterReplacement(self, s, k):
        #我觉得应该先确定窗口的长度。根据k的大小，我可以在第一个字母及其连续的情况下，额外加上k的长度
        #然后把最长的string的长度给记下来
        #以上都是正着想
        #要是反着想：就是贪心思维
        max_count = 0 #字符出现次数最多的字符 
        #那么我把剩下所有字符换成出现次数最多的字符，则需要L-max_count次
        #所以合法的路劲是只要L-max_count < k, 则窗口合法
        L = len(s)
        #快慢指针
        l,r = 0,0
        count = {}
        res = 0
        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0) + 1
            max_count = max(max_count, count[s[r]])
            while r-l+1-max_count > k:
                count[s[l]] -= 1
                l += 1
        res = r-l+1
        return res
        