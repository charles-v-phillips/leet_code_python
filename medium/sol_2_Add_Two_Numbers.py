from stuff.linked_list_stuff import ListNode
from typing import Optional
class Solution:
    @staticmethod
    def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # pointer = rv = ListNode()
        # q = 0
        # while l1 and l2:
        #     pointer.val += q
        #     q, r = divmod(l1.val + l2.val,10)
        #     pointer.val += r
        #     if pointer.val == 10:
        #         pointer.val = 0
        #         q = 1
        #
        #     if not l1.next:
        #         pointer.next = l2.next
        #     elif not l2.next:
        #         pointer.next = l1.next
        #     else:
        #         l1 = l1.next
        #         l2 = l2.next
        #         pointer.next = ListNode()
        #         pointer = pointer.next
        q = 0
        rv = l1
        while l1:
            l1.val +=q
            if l2:

                q,l1.val = divmod(l1.val + l2.val,10)
                # q, r = divmod(l1.val + l2.val,10)
                # l1.val += r
                if l1.val == 10:
                    l1.val = 0
                    q = 1
            else:

                if l1.val >= 10:
                    q,l1.val = divmod(l1.val,10)
                    if not l1.next and q:
                        l1.next = ListNode()

            if not l1.next:
                l1.next = l2.next
            elif l2:
                l1 = l1.next
                l2 = l2.next
            else:
                l1 = l1.next


        return rv





if __name__ == '__main__':
    print(Solution.addTwoNumbers(ListNode.make_linked_list([2,4,3]), ListNode.make_linked_list([5,6,4])))