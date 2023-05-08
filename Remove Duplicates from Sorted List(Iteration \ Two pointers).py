'''
Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.

 

Example 1:

Input: head = [1,1,2]
Output: [1,2]

Example 2:

Input: head = [1,1,2,3,3]
Output: [1,2,3]

 

Constraints:

    The number of nodes in the list is in the range [0, 300].
    -100 <= Node.val <= 100
    The list is guaranteed to be sorted in ascending order.
'''

# Solution 1: (Iterative)
# Time Complexity : O(n)
# Space Complexity : O(1)

def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nodeList = []
        dummy = cur = ListNode()

        while head:
            if head.val in nodeList:
                cur.next = head.next
            else:
                nodeList.append(head.val)
                cur.next = head
                cur = cur.next
            head = head.next
        return dummy.next
        
# Solution 2 : (Two Pointers)
# Time Complexity : O(n)
# Space Complexity : O(1)

def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        first, second = head, head.next if head else None
        while second:
            if first.val == second.val:
                second = second.next
                first.next = second
            else:
                first = second
                second = second.next
        return head
