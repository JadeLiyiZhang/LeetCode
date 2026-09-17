# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode | None) -> ListNode | None:
        dummy = ListNode(0)
        dummy.next = head
        cur = dummy
        while cur.next and cur.next.next:
            next_1 = cur.next
            next_2 = cur.next.next
            next_3 = cur.next.next.next
            cur.next = next_2
            next_2.next = next_1
            next_1.next = next_3
            cur = cur.next.next
        return dummy.next