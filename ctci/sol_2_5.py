from stuff.linked_list_stuff import ListNode
#yucky because overwrites data in head 1. should make an entirely new list
class Solution:


    def sum(self, head1, head2):
        q = 0
        head = head1
        while head1 and head2:
            head1.val += q
            q,r = divmod(head1.val + head2.val,10)
            head1.val += r
            if not head1.next:
                head1.next = head2.next
                break
            else:
                head1 = head1.next
                head2 = head2.next

        return head

class Solution2:
    def sum(self, head1, head2):
        pointer = rv = ListNode()
        q = 0
        while head1 and head2:
            rv.val += q
            q,r = divmod(head1.val + head2.val,10)
            rv.val += r
            rv.next = ListNode()

            if not head1.next:
                rv.next = head2.next
                break
            elif not head2.next:
                rv.next = head1.next
                break
            else:
                head1 = head1.next
                head2 = head2.next
                rv = rv.next


        return pointer

if __name__ == '__main__':
    Solution2().sum(ListNode.make_linked_list([7,1,6,1]),ListNode.make_linked_list([5,9,2]))
