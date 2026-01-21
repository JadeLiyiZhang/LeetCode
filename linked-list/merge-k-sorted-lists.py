# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        seq = 0

        for _list in lists:
            if _list:
                heapq.heappush(heap, (_list.val, seq, _list))
                seq += 1

        dummy = ListNode(0)
        cur = dummy

        while heap:
            val, seq, node = heapq.heappop(heap)
            cur.next = node
            cur = cur.next
            if node.next:
                heapq.heappush(heap, (node.next.val, seq, node.next))
                seq += 1
        
        return dummy.next