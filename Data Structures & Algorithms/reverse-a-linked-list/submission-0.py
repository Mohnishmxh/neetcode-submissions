# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        prev = None
        curr = head
        
        while curr:
            nxt = curr.next   # 1. Save the next node
            curr.next = prev  # 2. Reverse the link
            prev = curr       # 3. Move prev forward
            curr = nxt        # 4. Move curr forward
            
        return prev