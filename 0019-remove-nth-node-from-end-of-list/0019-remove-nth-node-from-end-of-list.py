class Solution(object):
    def removeNthFromEnd(self, head, n):
        dummy = ListNode(0, head)
        fast = head
        slow = dummy
        while n != 0:
            fast = fast.next
            n -= 1
        while fast:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        return dummy.next 