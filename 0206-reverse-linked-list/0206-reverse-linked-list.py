class Solution(object):
    def reverseList(self, head):
        current = head
        prev = None
        while current:
            nc = current.next
            current.next = prev
            prev = current
            current = nc
        return prev       