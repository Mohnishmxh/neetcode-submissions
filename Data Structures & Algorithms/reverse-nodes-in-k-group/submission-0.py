# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k == 1:
            return head
        
        dummy = ListNode(0, head)
        group_prev = dummy
        
        while True:
            # 1. Check if there are at least k nodes left to reverse
            cursor = group_prev
            for _ in range(k):
                cursor = cursor.next
                if not cursor:
                    return dummy.next
            
            # 2. Store the start of the next group
            group_next = cursor.next
            
            # 3. Reverse the current k nodes
            prev = group_next
            curr = group_prev.next
            for _ in range(k):
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            
            # 4. Connect the reversed group back to the previous part of the list
            temp = group_prev.next
            group_prev.next = prev
            group_prev = temp
            
        return dummy.next