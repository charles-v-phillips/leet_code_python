from stuff.linked_list_stuff import ListNode
from collections import defaultdict
class Solution:
    def deleteDuplicates(self, head):
        seen = defaultdict(int)
        dummy = ListNode(-1, head)
        first = head



        while first:
            if seen[first.val] > 0:
                first = first.next
                dummy.next = first

            else:
                seen[first.val] += 1
                first = first.next
                dummy = dummy.next



        return head




if __name__ == '__main__':
    print(Solution().deleteDuplicates(ListNode.make_linked_list([1,1,2,3,3])))

