# 6.逆序输出链表
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3],用python的list来储存数字
    def printListFromTailToHead(self, listNode):
        # write code here
        tmp=[]
        node = listNode
        while node !=None:
            tmp.append(node.val)
            node=node.next
        tmp.reverse()
        return tmp
    def printListFrontTailToHead2(self,listNode): # 递归实现
        if listNode.next:
            self.printListFrontTailToHead2(listNode.next)
        print(listNode.val)
solu = Solution()
a = ListNode(1)
a.next = ListNode(2)
a.next.next = ListNode(3)
# print(solu.printListFromTailToHead(a))
solu.printListFrontTailToHead2(a)