# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        front = back = dummy

        for _ in range(n + 1):
            front = front.next

        while front:
            front = front.next
            back = back.next

        back.next = back.next.next

        return dummy.next
