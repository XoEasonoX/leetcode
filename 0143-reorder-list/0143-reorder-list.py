class Solution(object):
    def reorderList(self, head):
        if not head or not head.next:
            return
        slow = head  #head = 1 2 3 4 5
        fast = head
        prev = None
        while fast and fast.next:
            fast = fast.next.next #fast = 5
            prev_slow = slow
            slow = slow.next #slow = 3 4 5
        prev_slow.next = None# 1 2
        while slow:
            current = slow.next
            slow.next = prev
            prev = slow
            slow = current #prev 5 4 3
        while prev:
            p = prev.next # 4 3         #3
            h = head.next # 2           #none
            head.next = prev #(1) 5 4 3   # (2) 4 3
            if not h:
                break
            prev.next = h # (5) 2 
            prev = p # (4) 3
            head = h # (2)
        return   
        """
        :type head: Optional[ListNode]
        :rtype: None Do not return anything, modify head in-place instead.
        """
        