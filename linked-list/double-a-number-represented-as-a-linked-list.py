# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode(next=head)
        carry = 0
        current = dummy_head
        while current.next:
            carry = (current.next.val * 2) // 10
            current.val = (current.val * 2) % 10 + carry
            current = current.next
        current.val = (current.val * 2) % 10
        
        return dummy_head if dummy_head.val else dummy_head.next