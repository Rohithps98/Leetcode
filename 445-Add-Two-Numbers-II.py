# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        st1,st2 = [], []
        while l1:
            st1.append(l1.val)
            l1 = l1.next
        while l2:
            st2.append(l2.val)
            l2 = l2.next
        carry = 0
        prev = None
        while st1 or st2 or carry:
            su = carry
            if st1:
                su+=st1.pop()
            if st2:
                su+=st2.pop()
            carry = su//10
            digit = su%10
            node = ListNode(digit)
            node.next = prev
            prev = node
        return prev