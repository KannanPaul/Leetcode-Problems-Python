'''
Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

 

Example 1:

Input: s = "leetcode"
Output: 0

Example 2:

Input: s = "loveleetcode"
Output: 2

Example 3:

Input: s = "aabb"
Output: -1

 

Constraints:

    1 <= s.length <= 105
    s consists of only lowercase English letters.

'''

# Solution 1:

# Time Complexity : O(n) & Space Complexity : o(n) where n - length of string

def firstUniqChar(self, s: str) -> int:
        freq_dict = {}
        n = len(s)

        for char in s:
            if char in freq_dict:
                freq_dict[char] += 1
            else:
                freq_dict[char] = 1
        
        for index in range(n):
            if freq_dict[s[index]] == 1:
                return index
        return -1
      
