#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/10 22:35
# @Author  : liupeiyu
# @File    : 回溯.py
# 判断一个矩阵是否有某一个特定的字符串序列，顺序遍历每一个元素，遍历到每一个元素的时候执行一遍dfs，出口函数包括两个，一个是遍历完，一个是找到元素
# 如果找到则返回true，如果没有找到但是遍历完了则是false
# self.dfs 定义为从i，j开始，在flag的状态下是不是完成了任务；
# 回溯法递归的本质是把flag+1作为一个参数，这样在false返回的时候flag还会保持原来的状态；
# 扩展条件包括三种情况：（1）在一定的范围内扩展比如！=0（2）达成某种条件扩展比如 myma[i] == path[i]（3）用没用过
class Solution:
    def hasPath(self,matrix,rows,cols,path):
        self.row = rows
        self.col = cols
        self.myma = [matrix[i*self.col:i*self.col+self.col] for i in range(rows)]
        self.path = path
        flag = 0

        for i in range(rows):
            for j in range(cols):
                if self.myma[i][j] == self.path[flag]:
                    if self.dfs(i,j,flag+1,[(i,j)]):
                        # flag += 1
                        return True
        return False

    def dfs(self,i,j,flag,pathdic):
        # 返回条件
        if flag > len(self.path) - 1:
            return True

        # 扩展条件
        if i!=0 and self.myma[i-1][j] == self.path[flag] and (i-1,j) not in pathdic:
            if self.dfs(i-1,j,flag+1,pathdic+[(i-1,j)]): # 为了保证回溯回来之前的flag没有被修改，所以应该是把flag放在下一层的返回判断之后
                # flag += 1
                return True
        if j!=0 and self.myma[i][j-1] == self.path[flag] and (i,j-1) not in pathdic:
            if self.dfs(i,j-1,flag+1,pathdic+[(i,j-1)]):
                # flag += 1
                return True
        if i!=self.row-1 and self.myma[i+1][j] == self.path[flag] and (i+1,j) not in pathdic:
            if self.dfs(i+1,j,flag+1,pathdic+[(i+1,j)]):
                # flag += 1
                return True
        if j!=self.col-1 and self.myma[i][j+1] == self.path[flag] and (i,j+1) not in pathdic:
            if self.dfs(i,j+1,flag+1,pathdic+[(i,j+1)]):
                # flag += 1
                return True

        return False
solu = Solution()
print(solu.hasPath("ABCESFCSADEE",3,4,"ABCB"))