class Solution(object):
    def twoSum(self, numbers, target):
        l, r = 0, len(numbers)-1
        if numbers[l] + numbers[r] == target:
            return [l+1, r+1]
        while numbers[l] + numbers[r] != target:
            if numbers[l] + numbers[r] < target:
                l += 1
            if numbers[l] + numbers[r] > target:
                r -= 1
        return [l+1, r+1]

                
             
        