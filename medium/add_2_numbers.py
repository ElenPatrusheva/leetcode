from typing import Optional
# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        fst = ListNode(0)
        last = fst
        residual = 0
        while (l1 is not None) or (l2 is not None):
            _sum = residual
            if l1 is not None:
                _sum += l1.val
                l1 = l1.next
            if l2 is not None:
                _sum += l2.val
                l2 = l2.next
            tmp = ListNode(_sum % 10, None)
            last.next = tmp
            last = tmp
            residual = _sum // 10
        if residual == 1:
            tmp = ListNode(1, None)
            last.next = tmp
        return fst.next


a3 = ListNode(3)
a2 = ListNode(4, a3)
a1 = ListNode(2, a2)

b3 = ListNode(4)
b2 = ListNode(6, b3)
b1 = ListNode(5, b2)


c = Solution().mergeTwoLists(a1, b1)
for i in range(5):
    print(c.val)
    print(c.next)
    c = c.next
