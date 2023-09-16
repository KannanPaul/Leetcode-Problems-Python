'''
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

 

Example 1:

Input: root = [3,9,20,null,null,15,7]
Output: 3

Example 2:

Input: root = [1,null,2]
Output: 2

 

Constraints:

    The number of nodes in the tree is in the range [0, 104].
    -100 <= Node.val <= 100


'''

# Solution 1: (Recursion - DFS)

# Time Complexity - O(num of nodes) as we are traversing all the nodes of the tree
# Space Complexity - O(height of the tree) for the recursive stack

def dfs(root, depth):
            if not root:
                return depth
            return max(dfs(root.left,depth+1),dfs(root.right,depth+1))
        return dfs(root, 0)

# Solution 2: DFS: Iterative, In-Order Traversal

def maxDepth(self, root: Optional[TreeNode]) -> int:
        stack = [[root, 1]]
        res = 0

        while stack:
            node, depth = stack.pop()
            if node:
                res = max(res, depth)
                stack.append([node.left, depth+1])
                stack.append([node.right, depth+1])
        return res
 
# Solution 3: (Iterative - BFS) - BFS: Iterative, Level Order Traversal

def maxDepth(self, root: Optional[TreeNode]) -> int:
        depth = 0
        level = [root] if root else []
        while level:
            depth += 1
            queue = []
            for node in level:
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                level = queue
        return depth
