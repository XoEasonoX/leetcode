class Solution(object):
    def detectCycle(self, head):
        fast = head 
        slow = head    
        cur  = head    
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:              
                while slow != cur:
                    cur = cur.next
                    slow = slow.next
                return cur
        return None   