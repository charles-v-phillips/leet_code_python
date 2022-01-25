
from stuff.linked_list_stuff import ListNode
class Solution:
    def swapPairs(self, head):
        dummy = ListNode(-1,head)
        prev_node = dummy

        while head and head.next:
            first_node = head
            second_node = head.next
            prev_node.next = second_node
            first_node.next = second_node.next
            second_node.next = first_node

            prev_node = first_node
            head = first_node.next
        return dummy.next


class Solution2:
    def swapPairs(self, head):
        if not head or not head.next:
            return head

        first_node = head
        second_node = head.next

        first_node.next = self.swapPairs(second_node.next)
        second_node.next = first_node

        return second_node






if __name__ == '__main__':
    print(Solution2().swapPairs(head = ListNode.make_linked_list([1,2,3,4])))

