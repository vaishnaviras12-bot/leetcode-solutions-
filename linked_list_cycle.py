#141. Linked List Cycle
#Time Complexity: O(n)
#Space Complexity: O(n)
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

from typing import Optional
from typing import List
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        curr=head
        visited= set()
        while curr:
            if curr in visited:
                return True
            visited.add(curr)
            curr=curr.next
        return False
