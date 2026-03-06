class Solution(object):
    def isPalindrome(self, s):
        L, r = 0, len(s)-1
        while L < r:          # 2. 没碰头就继续
        # 3. 过滤掉左边的杂质
            while L < r and not s[L].isalnum():
                L += 1
        # 3. 过滤掉右边的杂质
            while L < r and not s[r].isalnum():
                r -= 1
        # 4. 对比
            if s[L].lower() != s[r].lower():
                return False
        # 5. 各自推进一步
            L += 1
            r -= 1
        # 如果循环走完了都没返回 False，说明全对上了
        return True