import heapq

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode(0)
        curr = dummy
        heap = []
        
        # Initialize the heap with the head node of each non-empty list
        for i, l in enumerate(lists):
            if l:
                # Include the index 'i' in the tuple to prevent direct 
                # comparison of ListNode objects if values are identical
                heapq.heappush(heap, (l.val, i, l))
                
        # Process the heap until empty
        while heap:
            val, i, node = heapq.heappop(heap)
            curr.next = node
            curr = curr.next
            
            # If there is a next node in the same list, push it into the heap
            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))
                
        return dummy.next