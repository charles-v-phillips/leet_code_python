class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        s = ''
        while self:
            s += str(self.val) + ' -> '
            self  =self.next
        s += 'None'
        return s

    def make_linked_list(arr):
        head = ListNode(arr[0])
        dummy = head
        for i in range(1, len(arr)):
            dummy.next = ListNode(arr[i])
            dummy = dummy.next
        return head







