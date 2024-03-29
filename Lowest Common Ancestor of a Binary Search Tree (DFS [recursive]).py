'''
Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

 

Example 1:

Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
Output: 6
Explanation: The LCA of nodes 2 and 8 is 6.

Example 2:

Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
Output: 2
Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.

Example 3:

Input: root = [2,1], p = 2, q = 1
Output: 2

'''

# Solution 1 : DFS recursive
# Time Complexity: O(n) &  Space Complexity : O(n) where n  - no. of nodes

def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root == None or root == p or root == q:
            return root

        leftNode = self.lowestCommonAncestor(root.left, p, q)
        rightNode = self.lowestCommonAncestor(root.right, p, q)
        
        if leftNode and rightNode:
            return root
        return leftNode or rightNode 
      
   
# Solution 2 : Iterative 
def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
   while root:
      if root.val > p.val and root.val > q.val:
          root = root.left
      elif root.val < p.val and root.val < q.val:
          root = root.right
      else:
          return root
       
# Solution 3 : Recursive
def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
   if root == None or root ==p or root == q:
       return root
   if (max(p.val, q.val) < root.val):
       return self.lowestCommonAncestor(root.left, p, q)
   elif (min(p.val, q.val) > root.val):
       return self.lowestCommonAncestor(root.right, p, q)
   else:
       return root 
       
    



    
  
