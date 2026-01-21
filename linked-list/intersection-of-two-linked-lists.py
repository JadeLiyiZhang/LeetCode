# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        len_A = self.get_length(headA)
        len_B = self.get_length(headB)
        if len_A >= len_B:
            headA = self.move_forward(headA, len_A - len_B)
        else:
            headB = self.move_forward(headB, len_B - len_A)
        
        while headA and headB:
            if headA == headB:
                return headA
            else:
                headA = headA.next
                headB = headB.next
        
        return None


    def get_length(self, head):
        cur = head
        count = 0
        while cur:
            count += 1
            cur = cur.next
        return count

    def move_forward(self, head, step):
        while step > 0:
            head = head.next
            step -= 1
        return head