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
