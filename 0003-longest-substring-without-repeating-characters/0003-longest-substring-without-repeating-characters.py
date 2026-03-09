class Solution(object):
    def lengthOfLongestSubstring(self, s):
        #快慢指针？
        l, r = 0, 0
        seen = set()
        max_len = 0
        for r in range(len(s)):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            if s[r] not in seen:
                seen.add(s[r])
            max_len = max(max_len, r-l+1)
        return max_len
        