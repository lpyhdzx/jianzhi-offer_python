# 5.替换空格
# 其实替换空格的问题在python下可以直接用replace来解决但是为了说明剑指offer这个题的思想，这里举了一个合并字符串的例子，主要借鉴的就是
# 在数组插入问题中，从尾向头部插入的时候可以节省空间，并且时间复杂度是O(N)级别
class Solution:
    def Mergelist(self,a1,a2):
        lena1 = len(a1)
        a1 = a1 + [0]*len(a2)
        x = len(a1)-1
        i = lena1-1
        j = len(a2) - 1
        while i>=0 and j>=0:
            if a1[i] > a2[j]:
                a1[x] = a1[i]
                i -= 1
            else:
                a1[x] = a2[j]
                j -= 1
            x -= 1
        while j >= 0:
            a1[j] = a2[j]
            j -= 1
        return a1
solu = Solution()
print(solu.Mergelist([2,4,6],[1,3,5]))