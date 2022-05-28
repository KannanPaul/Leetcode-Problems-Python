'''
Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.
In other words, return true if one of s1's permutations is the substring of s2.

Example 1:
Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").

Example 2:
Input: s1 = "ab", s2 = "eidboaoo"
Output: false

#Solution 1:
Time complexity - O(l1+l2) - where l1 & l2 - lenght of string s1 & s2
Space complexity - O(1)
   
   def checkInclusion(self, s1: str, s2: str) -> bool:
        l1=[0]*26
        l2=[0]*26
        if len(s1)>len(s2):
            return False
        n=len(s1)
        for i in s1:
            l1[ord(i)-ord('a')]+=1
        for j in range(len(s2)):
            l2[ord(s2[j])-ord('a')]+=1
            if j >=n:
                l2[ord(s2[j-n])-ord('a')]-=1
            if l1==l2:
                return True
        return False
        
        
