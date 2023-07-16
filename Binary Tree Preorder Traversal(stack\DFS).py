'''
Given the root of a binary tree, return the preorder traversal of its nodes' values.

 
Example 1:

Input: root = [1,null,2,3]
Output: [1,2,3]

Example 2:

Input: root = []
Output: []

Example 3:

Input: root = [1]
Output: [1]

 

Constraints:

    The number of nodes in the tree is in the range [0, 100].
    -100 <= Node.val <= 100

Follow up: Recursive solution is trivial, could you do it iteratively?
'''

# Solution 1: (Iterative)

# Time Complexity - O(n) 
# Space Complexity - O(n) 
# Usage of stack's LIFO feature:

def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack=[root]
        res=[]
        while stack:
            cur_node = stack.pop()
            if cur_node:
                res.append(cur_node.val)
                stack.append(cur_node.right)
                stack.append(cur_node.left)
        return res

     
# Solution 2: (Depth First Search / Recursion)
# Time Complexity - O(n)
# Space Complexity - O(n) space (function call stack)
# Auxiliary Space: If we don’t consider the size of the stack for function calls then O(1) otherwise O(h) where h is the height of the tree. 
      
def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res=[]
        if root:
            res.append(root.val)
            res=res+self.preorderTraversal(root.left)
            res=res+self.preorderTraversal(root.right)
        return res
      
# Solution 3: (Morris Traversal)
# Time Complexity - O(n)
# Space Complexity - O(1)
