# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

        
    def reverseKNodes(self, head ,k):
        new_head = None
        cur = head
        while k:
            next_node = cur.next
            cur.next = new_head
            new_head = cur
            cur = next_node
            k -= 1
        return new_head

    def reverseKGroup(self, head: ListNode | None, k: int) -> ListNode | None:
        count = 0
        cur = head
        while count < k and cur:
            cur = cur.next
            count += 1
        
        if count == k:
            reversedHead = self.reverseKNodes(head, k)

            head.next = self.reverseKGroup(cur, k)
            return reversedHead
        return head