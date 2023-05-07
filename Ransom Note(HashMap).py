'''
Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.

 

Example 1:

Input: ransomNote = "a", magazine = "b"
Output: false

Example 2:

Input: ransomNote = "aa", magazine = "ab"
Output: false

Example 3:

Input: ransomNote = "aa", magazine = "aab"
Output: true

 

Constraints:

    1 <= ransomNote.length, magazine.length <= 105
    ransomNote and magazine consist of lowercase English letters.

'''

# Solution 1:
# Time complexity : O(m+n) where m - length of 'magazine' string and n - length of 'ransomNote' string
# Space complexity : O(m) 

def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazineDict = {}

        for str in magazine:
            if str in magazineDict:
                magazineDict[str] += 1
            else:
                magazineDict[str] = 1
        
        for str in ransomNote:
            if str in magazineDict and magazineDict[str] > 0:
                magazineDict[str] -= 1
            else:
                return False
        return True
      
      
