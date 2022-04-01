
#Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Need Copy and Paste the code below into the specific leetcode prompt to work -- issues with inputs in func
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]

        Original Post-https://stackoverflow.com/questions/22507197/merging-two-sorted-linked-lists-into-one-linked-list-in-python/40794749
        This solution seems to be highly memory efficient but is comparatively slow to the other submissions on LeetCode

        """

        # Handle Missing List Case
        if list1 is None:
            return list2
        elif list2 is None:
            return list1


        # Dummy Node in case there are no values in either input lists -- returns correct object even if empty
        tail = dummy = ListNode()

        while not (list1 is None or list2 is None):
            if list1.val < list2.val:
                current_node = list1
                list1 = list1.next
            else:
                current_node = list2
                list2 = list2.next

            # Mutate Dummy after moving to next val (one val per iteration, two lists only one gets next'd)
            dummy.next = current_node
            dummy = dummy.next #append to intermediate list

        dummy.next = list1 or list2 #whichever is not None

        # Return the Tail of the Dummy Node, should be sorted list
        return tail.next




# Test Variable & Driver Code
test_list1 = [1, 2, 4]
test_list2 = [1, 3, 4]

s = Solution()
print(s.mergeTwoLists(test_list1, test_list2))


