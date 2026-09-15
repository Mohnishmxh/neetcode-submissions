# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # Create a dummy node to handle edge cases easily
        dummy = ListNode(0, head)
        slow = dummy
        fast = dummy
        
        # Move fast n + 1 steps ahead to create the gap
        for _ in range(n + 1):
            fast = fast.next
            
        # Move both pointers until fast reaches the end
        while fast:
            slow = slow.next
            fast = fast.next
            
        # Skip the target node
        slow.next = slow.next.next
        
        return dummy.next