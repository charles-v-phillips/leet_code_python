from stuff.linked_list_stuff import ListNode
class Solution:

    def isPalindrome(self, head) -> bool:
        nums = []
        while head:
            nums.append(head.val)
            head = head.next

        if nums == list(reversed(nums)):
            return True
        return False





if __name__ == '__main__':
    print(Solution().isPalindrome(ListNode.make_linked_list([1,2,2,1])))