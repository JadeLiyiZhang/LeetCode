# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head
        count = 0
        cur = head
        while cur:
            count += 1
            cur = cur.next
        k = k % count
        if k == 0:
            return head 
        move = count - k
        cur_2 = head
        for i in range(move - 1):
            cur_2 = cur_2.next
        new_head = cur_2.next
        cur_2.next = None
        cur_3 = new_head
        while cur_3 and cur_3.next:
            cur_3 = cur_3.next
        cur_3.next = head
        return new_head



