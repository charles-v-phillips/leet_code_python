from stuff.linked_list_stuff import ListNode
from collections import deque
class Solution:
    def reverseList(self, head):
        s = deque()
        def helper(node):
            if not node:
                return s.popleft()
            s.append(node.val)
            node.val = helper(node.next)
            if s: return s.popleft()


        helper(head)
        return head

class Solution2:
    def reverseList(self, head):
        prev = None
        curr = head
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev





if __name__ == '__main__':
    Solution().reverseList(ListNode.make_linked_list([1,2,3,4]))


