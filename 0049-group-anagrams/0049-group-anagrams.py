class Solution(object):
    def groupAnagrams(self, strs):
        hashmap = {}
        
        for x in strs:
            # 第一步：把单词 x 拆开排序，再拼回去，作为“身份勋章”（Key）
            # 比如 x = "eat" -> sorted(x) 是 ['a', 'e', 't'] -> "".join(...) 变成 "aet"
            key = "".join(sorted(x)) #把list里面的string连起来
            
            # 第二步：看看这个“勋章”在不在哈希表里
            if key not in hashmap:
                # 如果是第一次见这个组合，给它开一个新列表（新桶）
                hashmap[key] = []
            
            # 第三步：把原始单词 x 扔进对应的桶里
            hashmap[key].append(x)
            
        # 第四步：我们要的是所有的桶，不需要那些 Key
        return list(hashmap.values())
