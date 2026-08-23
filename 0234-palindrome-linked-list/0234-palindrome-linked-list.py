class Solution(object):
    def isPalindrome(self, head):
        fast = head
        slow = head
        prev = None
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        while slow:
            cur = slow.next
            slow.next = prev
            prev = slow 
            slow = cur
        while prev:
            if head.val == prev.val:
                prev = prev.next
                head = head.next
            else:
                return False
        return True