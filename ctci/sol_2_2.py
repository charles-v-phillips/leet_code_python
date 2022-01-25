from stuff.linked_list_stuff import ListNode
class Solution:
    def returnKthToLast(self, node,k):
        size = 0
        dummy = node

        while dummy:
            size +=1
            dummy = dummy.next
        dummy = node
        for i in range(size-k):
            dummy = dummy.next
        return dummy.val



class Solution2:
    rv = None
    def helper(self,head,k):
        if not head:
            return 0

        val = 1 + self.helper(head.next,k)

        if val == k:
            self.rv = head
        return val

    def returnKthToLast(self, head, k):
        self.helper(head,k)
        return self.rv



if __name__ == '__main__':
    print(Solution2().returnKthToLast(ListNode.make_linked_list([1,2,3,4,5]),2).val)