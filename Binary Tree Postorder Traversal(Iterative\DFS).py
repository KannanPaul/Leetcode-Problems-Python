'''
Given the root of a binary tree, return the postorder traversal of its nodes' values.

 

Example 1:

Input: root = [1,null,2,3]
Output: [3,2,1]

Example 2:

Input: root = []
Output: []

Example 3:

Input: root = [1]
Output: [1]

 

Constraints:

    The number of the nodes in the tree is in the range [0, 100].
    -100 <= Node.val <= 100

 
Follow up: Recursive solution is trivial, could you do it iteratively?
'''

# Solution 1: (Iterative)

# Time Complexity - O(n) 
# Space Complexity - O(n) 

def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = []
        res = []
        cur = root
        while cur or stack:
            if cur:
                res = [cur.val] + res
                stack.append(cur)
                cur = cur.right
            else:
                cur = stack.pop()
                cur = cur.left
        return res
                
# Solution 2: (Depth First Search / Recursion)
# Time Complexity - O(n)
# Space Complexity - O(n) space (function call stack)

def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        res = []

        if root:
            res = res + self.postorderTraversal(root.left)
            res = res + self.postorderTraversal(root.right)
            res.append(root.val)
        return res
