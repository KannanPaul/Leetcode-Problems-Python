'''
Given the head of a singly linked list, return the middle node of the linked list.
If there are two middle nodes, return the second middle node.

Example 1:
Input: head = [1,2,3,4,5]
Output: [3,4,5]
Explanation: The middle node of the list is node 3.

Example 2:
Input: head = [1,2,3,4,5,6]
Output: [4,5,6]
Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.
'''

#solution 1:
#Complexity Analysis
   #Time Complexity: O(N)O(N)O(N), where NNN is the number of nodes in the given list.
   #Space Complexity: O(N)O(N)O(N), the space used by A.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
       r=[]
       while head !=None:
            r.append(head)
            head=head.next
       m=len(r)//2
          
       return r[m]

#solution 2:


