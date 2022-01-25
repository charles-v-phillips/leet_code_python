from stuff.linked_list_stuff import ListNode
class Solution:
    def swapNodes(self, head, k):
        l = 0

        dummy = head
        while dummy != None:
            l +=1
            dummy = dummy.next


        left_swap = head
        for i in range(k-1):
            left_swap = left_swap.next

        right_swap = head
        for i in range(l - k):
            right_swap = right_swap.next

        print('hi')


if __name__ == '__main__':
    print(Solution().swapNodes(ListNode.make_linked_list([1,2,3,4,5,6,7,8,9,10]),4))
