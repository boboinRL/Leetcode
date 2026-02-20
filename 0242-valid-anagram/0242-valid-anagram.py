class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        count = {}
        for x in s:
            count[x] = count.get(x,0) + 1 #find x, if x cannot been found, return 0, 核心就是记录字母出现的次数
        for y in t:
            if y not in count:
                return False
            else:
                count[y] -= 1
            
            if count[y] == 0:
                del count[y] #完全删除这个key
        return count == {}

            




        