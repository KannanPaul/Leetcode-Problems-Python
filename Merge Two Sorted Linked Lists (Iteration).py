'''
You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.
Return the head of the merged linked list.

Example 1:
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:
Input: list1 = [], list2 = []
Output: []

Example 3:
Input: list1 = [], list2 = [0]
Output: [0]
'''

#Solution -1 :(Iteration)
# dummy & cur pointer explanation -> https://stackoverflow.com/questions/58715870/explanation-about-dummy-nodes-and-pointers-in-linked-lists#:~:text=1%20Answer&text=dummy%20and%20cur%20both%20point,because%20it's%20the%20same%20list.&text=you're%20not%20creating%20a,pointer%20down%20the%20existing%20list

def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy=cur= ListNode(0)
        while list1 and list2:
            if list1.val < list2.val:
                cur.next=list1
                list1=list1.next
            else:
                cur.next=list2
                list2=list2.next
            cur=cur.next
        cur.next=list1 or list2
        return dummy.next
