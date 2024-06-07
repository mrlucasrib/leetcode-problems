# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # if head is None or head.next is None:
        #     return head
        # newHead = self.reverseList(head.next)

        # nextNode = head.next
        # nextNode.next = head
        # head.next = None


        # return newHead
        currNode = head
        prevNode = None
        while currNode:
            foward = currNode.next
            currNode.next = prevNode
            prevNode = currNode

            currNode = foward
    
        return prevNode