'''
Given a string s, you can transform every letter individually to be lowercase or uppercase to create another string.
Return a list of all possible strings we could create. Return the output in any order.

Example 1:
Input: s = "a1b2"
Output: ["a1b2","a1B2","A1b2","A1B2"]

Example 2:
Input: s = "3z4"
Output: ["3z4","3Z4"]
'''

# Solution 1- (Backtracking)
# Time complexity - 

def letterCasePermutation(self, s: str) -> List[str]:
        ans=[]
        def backtrack(sub='',i=0):
            if len(sub)==len(s):
                ans.append(sub)
            else:
                if s[i].isalpha():
                    backtrack(sub+s[i].swapcase(),i+1)
                backtrack(sub+s[i],i+1)
                
        backtrack()
        return ans


# Solution 2- (Backtracking)
# Tim Complexity is O(2^m*k), 
# where m is number of letters and k is length of all string: we have 2^m solutions, each of them has length k, 
# and what is important we never go to deadend, so all solutions we are trying to build will be added to final answer. 
# Space complexity is O(2^m*k) as well.

 def letterCasePermutation(self, s: str) -> List[str]:
        ans=[]
        
        def dfs(i,built):
            if i == len(s):
                ans.append(built)
                return
            if s[i].isalpha():
                dfs(i+1,built+s[i].lower())
            dfs(i+1,built+s[i].upper())
        
        dfs(0,'')
        return ans
