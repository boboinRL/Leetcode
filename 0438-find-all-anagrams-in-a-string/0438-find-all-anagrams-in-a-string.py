class Solution(object):
    def findAnagrams(self, s, p):
        res = []
        if len(p) > len(s):
            return []
        p_count = {}
        #1. 统计p的字母频率
        for char in p:
            p_count[char] = p_count.get(char, 0) + 1 #对于p的字典的value里面加频率
        #2. 初始化窗口
        s_count = {}
        #for循环来框住前len(p)长度的字符
        for i in range(len(p)):
            s_count[s[i]] = s_count.get(s[i],0) + 1
        #3. 开始滑动
        #就看是不是完全match
        for i in range(len(p), len(s), 1):
            if s_count == p_count:
                res.append(i-len(p))
            s_count[s[i]] = s_count.get(s[i],0) + 1
            s_count[s[i-len(p)]] -= 1
            if s_count[s[i-len(p)]] == 0:
                del s_count[s[i-len(p)]]#这一步很重要，如果value为0了，就得先删除，不然在字典里面就是不一样的
        if s_count == p_count:
            res.append(len(s)-len(p))#我一开始这里没有理解到位
            #这里实际上等循环结束之后，对比最后一个窗口
            #因为这里是先比较，再移动的窗口，所以导致最后一个窗口并不会被检查到
        return res
            
            
