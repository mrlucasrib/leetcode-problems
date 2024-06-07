# https://leetcode.com/problems/merge-two-sorted-lists/description/
# Definition for singly-linked list.
from typing import Optional, List
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    @staticmethod
    def from_array(arr: List[int]):
        head = ListNode()
        it = head
        for i in arr:
            it.val = i
            it.next = ListNode()
            it = it.next
        return head

            
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
#         ans = ListNode()
#         headAns = ans
#         currNodeList1 = list1
#         currNodeList2 = list2
#         if currNodeList1 is None or currNodeList2 is None:
#             return currNodeList1 if currNodeList2 is None else currNodeList2
#         while True: 
#             if currNodeList1.val  > currNodeList2.val:
#                 ans.next = currNodeList2
#                 currNodeList2 = currNodeList2.next
#             else:
#                 ans.next = currNodeList1
#                 currNodeList1 = currNodeList1.next
#             ans = ans.next
#             if currNodeList1 is None:
#                 ans.next = currNodeList2
#                 break
#             elif currNodeList2 is None:
#                 ans.next = currNodeList1
#                 break
#         return headAns.next
# print(Solution().mergeTwoLists(ListNode.from_array([1,2,4]),ListNode.from_array([1,3,4])))

# recursive approach
        if list1 is None: # or list is None:
            return list2
        elif list2 is None:
            return list1
        
        if list1.val <= list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2
print(Solution().mergeTwoLists(ListNode.from_array([1,2,4]),ListNode.from_array([1,3,4])))

