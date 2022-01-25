from stuff.linked_list_stuff import ListNode
class Solution:
    def addTwoNumbers(self, l1, l2) :
        pointer = rv = ListNode()
        q = 0
        while l1 and l2:
            rv.val += q
            q, r = divmod(l1.val + l2.val, 10)
            rv.val += r

            rv.next = ListNode()

            if not l1.next:
                l1.next = ListNode()
                l1 = l1.next
                l2 = l2.next
                rv = rv.next
                # rv.next = l2.next
                break
            elif not l2.next:
                l2.next = ListNode()
                l2 = l2.next
                l1 = l1.next
                rv = rv.next
                # rv.next = l1.next
                # break
            else:
                l1 = l1.next
                l2 = l2.next
                rv = rv.next

        return pointer

class Solution2:
    def addTwoNumbers(self, l1, l2):
        rv = pointer = ListNode()
        q = 0
        while l1 and l2:
            rv.val +=q
            q,r =divmod(l1.val + l2.val ,10)
            rv.val += r

            if not l1.next and not l2.next:
                break
            elif l1.next and l2.next:
                l1 = l1.next
                l2 = l2.next
                rv.next = ListNode()
                rv = rv.next

            elif not l1.next:
                l1.next = ListNode()
                l1 = l1.next
                l2 = l2.next
                rv.next = ListNode()
                rv = rv.next

            elif not l2.next:
                l2.next = ListNode()
                l2 = l2.next
                l1 = l1.next
                rv.next = ListNode()
                rv = rv.next


        return pointer


if __name__ == '__main__':
    print(Solution2().addTwoNumbers(ListNode.make_linked_list([9,9,9,9,9,9,9]), ListNode.make_linked_list([9,9,9,9])))