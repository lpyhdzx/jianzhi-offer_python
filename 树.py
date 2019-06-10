#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/9 23:18
# @Author  : liupeiyu
# @File    : 树.py
# 7.重建二叉树，用前序和中序遍历重建

#这里用的pre.pop的方法挺好，写起来很简单，因为在左子树的时候，pop出来了所有左子树的节点，再到右子树的时候就剩下了其余的节点
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        # 是则返回，一直到最后的空的时候就是null节点
        if not pre or not tin:
            return None
        # do
        root = TreeNode(pre.pop(0)) #这里必须定义一个node
        index = tin.index(root.val) # 找root节点的index，然后判断左子树的list和右子树的list
        # 否则扩展
        root.left = self.reConstructBinaryTree(pre, tin[:index]) #每次做左子树的时候会把节点都pop完，剩下的就是右子树的了
        root.right = self.reConstructBinaryTree(pre, tin[index + 1:])