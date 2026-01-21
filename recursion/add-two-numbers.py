# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        cur = dummy
        carry = 0
        p, q = l1, l2

        while p or q or carry:
            s = carry
            if p:
                s += p.val
                p = p.next
            if q:
                s += q.val
                q = q.next
            carry, digit = divmod(s, 10)   # digit = s % 10, carry = s // 10
            cur.next = ListNode(digit)
            cur = cur.next

        return dummy.next
