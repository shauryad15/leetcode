class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        current = dummy
        p1, p2 = l1, l2
        carry = 0
        
        while p1 or p2:
            digit1 = p1.val if p1 else 0
            digit2 = p2.val if p2 else 0
            
            sum_val = digit1 + digit2 + carry
            carry = sum_val // 10
            sum_val = sum_val % 10
            
            current.next = ListNode(sum_val)
            current = current.next
            
            if p1:
                p1 = p1.next
            if p2:
                p2 = p2.next
        
        if carry > 0:
            current.next = ListNode(carry)
        
        return dummy.next

      