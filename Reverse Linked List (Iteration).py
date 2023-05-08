'''
Given the head of a singly linked list, reverse the list, and return the reversed list.

Example 1:
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Example 2:
Input: head = [1,2]
Output: [2,1]

Example 3:
Input: head = []
Output: []
'''

#Solution - 1: Recursion
#Time complexity - O(n)
# Space complexity - 

def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    return self._reverse(head) 
    
def _reverse(self, node, prev=None):
    if not node:
       return prev
    n=node.next
    node.next=prev
    return self._reverse(n,node)

#Solution - 2: (Iteration)
# Time complexity - O(n)
# Space complexity - O(1) 

def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev= None
        while head:
            cur= head
            head=head.next
            cur.next=prev
            prev=cur
        return prev
