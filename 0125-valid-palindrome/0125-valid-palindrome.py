class Solution(object):
    def isPalindrome(self, s):
        new_s = ""
        for n in s:
            if n.isalnum():
                new_s = new_s + lower(n)
        return new_s == new_s[::-1]