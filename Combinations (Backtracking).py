'''
Given two integers n and k, return all possible combinations of k numbers out of the range [1, n].
You may return the answer in any order.

Example 1:
Input: n = 4, k = 2
Output:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]

Example 2:
Input: n = 1, k = 1
Output: [[1]]
'''

#Solution - 1 : 
# Time Complexity: O(n!/k!(n-k)!), or mathematically n choose k.
# Recursive Space Complexity: O(n!/k!(n-k)!)

def combine(self, n: int, k: int) -> List[List[int]]:
        sol=[]
        def backtrack(remain,comb,nex):
            if remain==0:
                sol.append(comb.copy())
            else:
                for i in range(nex,n+1):
                    comb.append(i)
                    backtrack(remain-1,comb,i+1)
                    comb.pop()
                    
        backtrack(k,[],1)
        return sol
