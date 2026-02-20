class Solution(object):
    def subarraySum(self, nums, k):
        #逻辑是要避免重复计算，我把每个子集计算之后，任何子集和都可以用不同子集给算出来（前缀和思维）
        #相当于我现在有一个累计的和，如果我想要知道某个子集的sum（k），就用cur_sum（已知）-pre_sum（未知） = k（已知）
        #又把这个问题变成一个次数问题了看有多少个子集和可以用cur_sum-k表达出来（实际为次数）
        cur_sum = 0
        count = 0 
        hashmap = {0: 1}
        for i in nums:
            cur_sum += i
            #查pre_sum 有没有等于cur_sum - k
            pre_sum = cur_sum - k
            if pre_sum in hashmap:
                #如果在hashmap中，那么count次数要加: count + hashmap当中已有的次数
                #可是给我们还要确定用哪个key的value，应该是pre_sum的value(次数)
                count = count + hashmap[pre_sum]
            #然后还要把新的cur_sum 存入hashmap, 无论啥情况，都要把最新的累计和放进hashmap
            #hashmap[cur_sum] = 1, 我不能简单粗暴的设为1
            #get function很好用，因为要防止cur_sum和之前的cur_sum相同，就得用get来找是否有一样的cur_sum
            hashmap[cur_sum] = hashmap.get(cur_sum, 0) + 1
        return count
            



        

        