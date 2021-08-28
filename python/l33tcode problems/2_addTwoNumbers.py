# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        # 1. Create a new ListNode and a dummy ListNode. The dummy node will allow me to add more and more nodes to the same origin (l3)
        l3_dummy = ListNode(0)
        l3 = l3_dummy
        carry = 0
        
        # 2. Do at least once: loop through l1 and l2 adding their digits together along with the carry bit if necessary
        while True:
            sum = l1.val + l2.val + carry
            if sum > 9:
                carry = 1
                l3.next = ListNode(sum-10)
            else:
                carry = 0
                l3.next = ListNode(sum)
                
            l3 = l3.next
            # 3. Move along to next node in l1 and l2, if at the end then assign them the value of 0
            l1 = l1.next if l1.next else ListNode(0)
            l2 = l2.next if l2.next else ListNode(0)
            
            # 4. Messy break clause, want to come back and refine. Ends when l1 and l2 are 0 and have no .next, and there is no carry bit
            if l1.val == 0 and l2.val == 0 and not l1.next and not l2.next and not carry:
                return l3_dummy.next
            