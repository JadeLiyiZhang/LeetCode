# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return
        
        dummy_node = ListNode(0)
        dummy_node.next = head
        current_node = head
        prev_node = dummy_node

        while(current_node):
            if current_node.next and current_node.val == current_node.next.val:
                while current_node.next and current_node.val == current_node.next.val:
                    current_node = current_node.next
                prev_node.next = current_node

            prev_node = prev_node.next
            current_node = current_node.next

        return dummy_node.next