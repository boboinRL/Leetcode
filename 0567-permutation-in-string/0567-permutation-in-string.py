class Solution(object):
    def checkInclusion(self, s1, s2):
        #I think dict need to be used
        res = []
        if len(s1) > len(s2):
            return False
        #先统计s1里面的字符频次
        s1_count = {}
        for i in s1:
            s1_count[i] = s1_count.get(i, 0) + 1 #本质是在找key
        #创建一个固定长度为s1的窗口
        s2_count = {}
        for j in range(len(s1)):
            s2_count[s2[j]] = s2_count.get(s2[j], 0) + 1
        #然后就往后挪，在固定相连窗口里面找是否有相同&相连的字母
        for i in range(len(s1), len(s2), 1):
            if s1_count == s2_count:
                return True
            s2_count[s2[i]] = s2_count.get(s2[i], 0) + 1
            s2_count[s2[i-len(s1)]] -= 1
            if s2_count[s2[i-len(s1)]] == 0:
                del s2_count[s2[i-len(s1)]]
        if s1_count == s2_count:
            return True
        else:
            return False
        

        