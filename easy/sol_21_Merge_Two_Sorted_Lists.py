from stuff.linked_list_stuff import ListNode
# Iteration
class Solution:
    def mergeTwoLists(self, list1, list2):
        less, more = (list1,list2) if list1.val <= list2.val else (list2,list1)
        less_dummy = less

        while more != None:
            while  less_dummy.next != None and less_dummy.next.val < more.val:
                less_dummy = less_dummy.next
            insert = more
            more = more.next
            insert.next = less_dummy.next
            less_dummy.next = insert

        return less



#Recursion
class Solution2:
    def mergeTwoLists(self, list1, list2):
        if list1 == None:
            return list2
        elif list2 == None:
            return list1

        elif list1.val < list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list2.next,list1)
            return list2




if __name__ == '__main__':

    list = Solution2().mergeTwoLists(ListNode.make_linked_list([-9,3]), ListNode.make_linked_list([5,7]))
    print('HI')