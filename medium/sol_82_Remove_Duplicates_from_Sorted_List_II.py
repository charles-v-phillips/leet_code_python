from stuff.linked_list_stuff import ListNode
from collections import defaultdict
class Solution:
    def deleteDuplicates(head):
        sentinal = ListNode(float('inf'), head)
        pred = head
        while head:
            if head.next and head.val == head.next.val:
                while head.next and head.val == head.next.val:
                    head = head.next
                pred.next = head.next
            else:
                pred = pred.next

            head = head.next



        return sentinal.next




if __name__ == '__main__':
     print(Solution.deleteDuplicates(ListNode.make_linked_list([1,2,3,3,4,4,5])))






