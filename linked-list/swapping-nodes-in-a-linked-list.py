# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, next=head)
        cur = dummy
        for i in range(k):
            cur = cur.next
        left_val = cur.val
        
        fast, slow = dummy, dummy
        for j in range(k):
            fast = fast.next
        while fast:
            slow = slow.next
            fast = fast.next
        right_val = slow.val
        cur.val = right_val
        slow.val = left_val
        return dummy.next
        
        