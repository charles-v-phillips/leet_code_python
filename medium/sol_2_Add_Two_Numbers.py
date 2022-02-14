from stuff.linked_list_stuff import ListNode
from typing import Optional
class Solution:
    @staticmethod
    def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode()
        p, q, curr = l1, l2, dummy_head
        carry = 0
        while p is not None or q is not None:
            x = p.val if p is not None else 0
            y = q.val if q is not None else 0

            carry, value = divmod(carry + x + y, 10)
            curr.next = ListNode(value)
            curr = curr.next

            p = p.next if p else p
            q = q.next if q else q

        if carry:
            curr.next = ListNode(carry)

        return dummy_head.next








if __name__ == '__main__':
    print(Solution.addTwoNumbers(ListNode.make_linked_list([2,4,3]), ListNode.make_linked_list([5,6,4])))