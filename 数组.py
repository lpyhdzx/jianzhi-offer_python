# 4.二维数组中的查找
class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        rl=len(array)
        cl=len(array[0])
        i=0
        j=cl-1
        while i < rl:
            while j>-1:
                if array[i][j]==target:
                    return True
                elif array[i][j]<target:
                    i=i+1
                    break
                else:
                    j=j-1
        return False
solu = Solution()
print(solu.Find(4,[[1,2,8,9],[2,4,9,12]]))

# 总结：
# 题目类型：查找问题
# 关键：从右上角开始查找，这样可以最大化的排除尽可能更多的列
# 方法：需要通过一开始的模拟找到解决方法的突破点