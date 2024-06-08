# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        middle = head
        counter = 1
        currentMiddlePosition = 1
        if head and not head.next:
            return head
        while curr:
            mid = counter//2+1
            if currentMiddlePosition != mid:
                middle = middle.next
                currentMiddlePosition += 1
            curr = curr.next
            counter += 1
        return middle
        