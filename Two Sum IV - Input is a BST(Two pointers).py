'''
Given the root of a binary search tree and an integer k, return true if there exist two elements in the BST such that their sum is equal to k, or false otherwise.

Example 1:

Input: root = [5,3,6,2,4,null,7], k = 9
Output: true

Example 2:

Input: root = [5,3,6,2,4,null,7], k = 28
Output: false

'''

# Solution 1 : Stack (Interviewer expects this solution)

# Time: O(N), where N is the number of nodes in the BST.
# Space: O(H), where H is the height of the BST. The size of stack is up to O(H).


def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        def leftNode(lleft, root):
            while root:
                lleft.append(root)
                root = root.left
        
        def rightNode(lright, root):
            while root:
                lright.append(root)
                root = root.right
            
        def nextLeft(lleft):
            node = lleft.pop()
            leftNode(lleft, node.right)
            return node.val
        
        def nextRight(lright):
            node = lright.pop()
            rightNode(lright, node.left)
            return node.val


        listLeft , listRight = [], []
        leftNode(listLeft, root)
        rightNode(listRight, root)

        left, right = nextLeft(listLeft), nextRight(listRight)

        while left < right:
            if left + right == k:
                return True
            if left + right < k:
                left = nextLeft(listLeft)
            else:
                right = nextRight(listRight)
        return False

