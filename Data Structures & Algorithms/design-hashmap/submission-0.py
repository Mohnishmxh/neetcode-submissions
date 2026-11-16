class ListNode:
    def __init__(self, key: int = -1, val: int = -1, next_node=None):
        self.key = key
        self.val = val
        self.next = next_node


class MyHashMap:
    def __init__(self):
        # A prime number reduces hash collisions
        self.size = 2069
        # Initialize each bucket with a dummy head node
        self.buckets = [ListNode() for _ in range(self.size)]

    def _hash(self, key: int) -> int:
        return key % self.size

    def put(self, key: int, value: int) -> None:
        index = self._hash(key)
        curr = self.buckets[index]

        # Traverse the chain to check if the key already exists
        while curr.next:
            if curr.next.key == key:
                curr.next.val = value  # Update existing value
                return
            curr = curr.next

        # Key not found; append a new node at the end of the chain
        curr.next = ListNode(key, value)

    def get(self, key: int) -> int:
        index = self._hash(key)
        curr = self.buckets[index].next  # Skip the dummy head

        while curr:
            if curr.key == key:
                return curr.val
            curr = curr.next

        return -1

    def remove(self, key: int) -> None:
        index = self._hash(key)
        curr = self.buckets[index]

        while curr.next:
            if curr.next.key == key:
                # Bypass the target node to remove it
                curr.next = curr.next.next
                return
            curr = curr.next