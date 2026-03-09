class Solution(object):
    def moveZeroes(self, nums):
        #实际上是考快慢指针
        l, r = 0, 0
        #r be fast pointer, l be slow pointer
        #if r find non-zero elements, give it to l
        for r in range(len(nums)):
            if nums[r] == 0:
                r += 1
            else:
                #here is something wrong
                #I wangt exchange these two values
                #but i have to replace the last two figures
                a = nums[l]
                nums[l] = nums[r]
                nums[r] = a
                l += 1
            