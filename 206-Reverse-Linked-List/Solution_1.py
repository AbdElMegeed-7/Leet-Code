# 206-Reverse-Linked-List #
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        previous = None
        current = head

        while current:
            next = current.next
            current.next = previous
            previous = current
            current = next

        return previous