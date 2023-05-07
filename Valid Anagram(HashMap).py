'''
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true

Example 2:

Input: s = "rat", t = "car"
Output: false

 

Constraints:

    1 <= s.length, t.length <= 5 * 104
    s and t consist of lowercase English letters.

 '''

# Solution 1 :

def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
      
        def freq(strlist):
            strdict=dict()
            for str in strlist:
                if str in strdict:
                    strdict[str]+=1
                else:
                    strdict[str]=1
            return strdict

        if freq(s) == freq(t):
            return True
        else:
            return False

# Solution 2 :

def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        sdict = {}
        for str in s:
            if str in sdict:
                sdict[str] += 1
            else:
                sdict[str] = 1
        
        for str in t:
            if not str in sdict:
                return False
            elif sdict[str] == 0:
                return False
            sdict[str] -= 1
        
        return True
