# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/description/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Solution:
    foundP = False
    foundQ = False
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        dequeP = deque()
        dequeQ = deque()
        minNode = root
        self.dfs(root, p, q, dequeP, dequeQ)
        print(list([x.val for x in dequeQ]))
        print(list([x.val for x in dequeP]))
        # print(dequeQ)
        # comparar deque 1 e deque 2
        while dequeP and dequeQ:
            itemP = dequeP.popleft()
            itemQ = dequeQ.popleft()
            if itemP.val == itemQ.val:
                minNode = itemP
        return minNode

    def dfs(self, actualNode, p, q, dequeP, dequeQ):
        if actualNode is None:
            return
        if self.foundP and self.foundQ:
            return
        if not self.foundP:
            dequeP.append(actualNode)
        if not self.foundQ:
            dequeQ.append(actualNode)
        if actualNode.val == p.val:
            self.foundP = True

        if actualNode.val == q.val:        
            self.foundQ = True


        self.dfs(actualNode.left, p, q, dequeP, dequeQ)
        self.dfs(actualNode.right, p, q, dequeP, dequeQ)
        if not self.foundP:
            dequeP.pop()
        if not self.foundQ:
            dequeQ.pop()