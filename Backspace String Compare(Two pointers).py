'''
Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.

Note that after backspacing an empty text, the text will continue empty.

 

Example 1:

Input: s = "ab#c", t = "ad#c"
Output: true
Explanation: Both s and t become "ac".

Example 2:

Input: s = "ab##", t = "c#d#"
Output: true
Explanation: Both s and t become "".

Example 3:

Input: s = "a#c", t = "b"
Output: false
Explanation: s becomes "c" while t becomes "b".

 

Constraints:

    1 <= s.length, t.length <= 200
    s and t only contain lowercase letters and '#' characters.
'''

# Solution 1 : (Brute force solution)

# Time complexity: O(S+T)
# Space complexity: O(S+T)
# where S & T - lenth of given strings S, T

def backspaceCompare(self, S: str, T: str) -> bool:
        def fn(a):
            b=''
            for i in range(0,len(a)):
                if a[i] != '#':
                    b=b+a[i]
                else:
                    b=b[:-1]
            return b

        c=fn(S)
        d=fn(T)
        if c==d:
            return True
        else:
            return False

# Solution 2: (Brute force solution)
def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        sL = list(s)
        tL = list(t)

        sStack = []
        tStack = []

        index = 0
        while index < len(sL) or index < len(tL):
            sCurr = sL[index] if index < len(sL) else ""
            tCurr = tL[index] if index < len(tL) else ""

            if sCurr == "#":
                if len(sStack) != 0: sStack.pop()
            else:
                sStack.append(sCurr)
            if tCurr == "#":
                if len(tStack) != 0: tStack.pop()
            else:
                tStack.append(tCurr)
            index += 1
        return "".join(sStack) == "".join(tStack)

# Solution 3 : (Optimal solution using Two Pointers)
# Time complexity: O(s+t)
# Space complexity: O(1)
# where S & T - lenth of given strings S, T

  def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
    
        p1 = len(s)-1   
        p2 = len(t)-1   
        while p1 >=0 or p2 >= 0:
            if (p1 >= 0 and s[p1] == '#') or (p2 >= 0 and t[p2] =='#'):
                if s[p1] =='#':
                    backcount = 2
                    while backcount > 0:
                        p1 -=1   
                        backcount -= 1   
                        if p1 >=0 and s[p1] == '#':
                            backcount += 2
                if t[p2] =='#':
                    backcount = 2 
                    while backcount > 0:
                        p2 -=1
                        backcount -= 1
                        if p2 >= 0 and t[p2] =='#':
                            backcount +=2
            else:
                if p1 <0 or p2 <0:
                    return False
                elif s[p1] != t[p2]:
                    return False
                else:
                    p1 -= 1
                    p2 -= 1
        return True


