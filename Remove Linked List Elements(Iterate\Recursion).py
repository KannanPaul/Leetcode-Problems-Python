'''
Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, and return the new head.

 

Example 1:

Input: head = [1,2,6,3,4,5,6], val = 6
Output: [1,2,3,4,5]

Example 2:

Input: head = [], val = 1
Output: []

Example 3:

Input: head = [7,7,7,7], val = 7
Output: []

 

Constraints:

    The number of nodes in the list is in the range [0, 104].
    1 <= Node.val <= 50
    0 <= val <= 50

'''

# Solution 1:
# Time complexity - O(n) --> Each Node in the list is visited once.
# Space Complexity: O(1) --> Contant space is used for this solution

def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if not head:
            return
        dummy = cur = ListNode()
        while head:
            if head.val != val:
                cur.next = head
                cur = cur.next
            elif head.val == val:
                cur.next = head.next
            head = head.next
        return dummy.next
