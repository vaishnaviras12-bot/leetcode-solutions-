# 21. Merge Two Sorted Lists
#Time Complexity: O(n+m) where n and m are the lengths of the two lists.
#Space Complexity: O(1)
from typing import Optional
from typing import List
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode(0)
        tail=dummy
        while list1 and list2:
            if list1.val>list2.val:
                tail.next=list2
                list2=list2.next
            else:
                tail.next=list1
                list1=list1.next
            tail=tail.next
        tail.next=list1 if list1 else list2
        return dummy.next