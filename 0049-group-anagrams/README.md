<h2><a href="https://leetcode.com/problems/group-anagrams">49. Group Anagrams</a></h2><h3>Medium</h3><hr><p>Given an array of strings <code>strs</code>, group the <span data-keyword="anagram">anagrams</span> together. You can return the answer in <strong>any order</strong>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">strs = [&quot;eat&quot;,&quot;tea&quot;,&quot;tan&quot;,&quot;ate&quot;,&quot;nat&quot;,&quot;bat&quot;]</span></p>

<p><strong>Output:</strong> <span class="example-io">[[&quot;bat&quot;],[&quot;nat&quot;,&quot;tan&quot;],[&quot;ate&quot;,&quot;eat&quot;,&quot;tea&quot;]]</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>There is no string in strs that can be rearranged to form <code>&quot;bat&quot;</code>.</li>
	<li>The strings <code>&quot;nat&quot;</code> and <code>&quot;tan&quot;</code> are anagrams as they can be rearranged to form each other.</li>
	<li>The strings <code>&quot;ate&quot;</code>, <code>&quot;eat&quot;</code>, and <code>&quot;tea&quot;</code> are anagrams as they can be rearranged to form each other.</li>
</ul>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">strs = [&quot;&quot;]</span></p>

<p><strong>Output:</strong> <span class="example-io">[[&quot;&quot;]]</span></p>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">strs = [&quot;a&quot;]</span></p>

<p><strong>Output:</strong> <span class="example-io">[[&quot;a&quot;]]</span></p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= strs.length &lt;= 10<sup>4</sup></code></li>
	<li><code>0 &lt;= strs[i].length &lt;= 100</code></li>
	<li><code>strs[i]</code> consists of lowercase English letters.</li>
</ul>
这个题虽然有难度，但我的思路是对的：我有一个一维数组，我要把一维数组里面的每个元素通过排序（Standardization）找到它的标识，再把互为变位词（Anagram）的元素放进同一个哈希表中，最终组成一个二维数组。

```python
class Solution(object):
    def groupAnagrams(self, strs):
        # 结果存放在 hashmap 中
        # key: 重新排序后的字符串 (唯一标识)
        # value: 原字符串组成的列表
        hashmap = {}
        
        for x in strs:
            # 这里的处理很关键：
            # 1. sorted(x) 会把字符串拆成字符列表并排序，例如 "eat" -> ['a', 'e', 't']
            # 2. "".join(...) 把列表重新拼回字符串，作为字典不可变的 key
            key = "".join(sorted(x))
            
            # 如果这个标识还没出现过，初始化一个空列表
            if key not in hashmap:
                hashmap[key] = []
            
            # 将原始字符串 x 加入到对应的组里
            hashmap[key].append(x)
            
        return list(hashmap.values())

直觉就知道sorted（strs[i]) 这个地方没有写对，没有变量可以赋予给新产生的内容
