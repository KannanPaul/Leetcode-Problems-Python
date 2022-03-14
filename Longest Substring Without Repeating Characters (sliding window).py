'''
Given a string s, find the length of the longest substring without repeating characters.

Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.

Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
'''

#Solution 1:
s = "abcabcbb"
charindex={}
maxlen=0
start=0
for i in range(len(s)):
  if s[i] in charindex and start <= charindex[s[i]]:
    start=charindex[s[i]]+1
  else:
    maxlen=max(maxlen,i-start+1)
  charindex[s[i]]=i
        
print(maxlen)

#Solution 2:
s = "abcabcbb"
strindex={}
l=0
output=0
for r in range(len(s)):
  if s[r] not in strindex:
    output=max(output,r-l+1)
  else:
    if strindex[s[r]] <l:
      output=max(output,r-l+1)
    else:
      l=strindex[s[r]]+1
  strindex[s[r]]=r
  
print(output)
