'''
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

 

Example 1:

Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.

Example 2:

Input: nums1 = [1], m = 1, nums2 = [], n = 0
Output: [1]
Explanation: The arrays we are merging are [1] and [].
The result of the merge is [1].

Example 3:

Input: nums1 = [0], m = 0, nums2 = [1], n = 1
Output: [1]
Explanation: The arrays we are merging are [] and [1].
The result of the merge is [1].
Note that because m = 0, there are no elements in nums1. The 0 is only there to ensure the merge result can fit in nums1.

 

Constraints:

    nums1.length == m + n
    nums2.length == n
    0 <= m, n <= 200
    1 <= m + n <= 200
    -109 <= nums1[i], nums2[j] <= 109

 

Follow up: Can you come up with an algorithm that runs in O(m + n) time?

'''

# Solution 1 :

# Time complexity = O(k), k = m + n; 
# Space complexity = O(1);

def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        while n>0:
            if m>0 and nums1[m-1] > nums2[n-1]:
                nums1[m+n-1] = nums1[m-1]
                m = m-1
            else:
                nums1[m+n-1] = nums2[n-1]
                n = n-1

Variation 2:
Given two non-decreasing sorted arrays, ‘A’ and ‘B’, having ‘N’ and ‘M’ elements, respectively.
You must merge these arrays, ‘A’ and ‘B’, into a sorted array without using extra space. Of all the 'N + M' sorted elements, array 'A' should contain the first 'N' elements, and array 'B' should have the last 'M' elements.

Note:
You must perform the merge operation in place and must not allocate any extra space to merge the two arrays.

For example:
When ‘N’ = 4, ‘A’ = {1, 4, 5, 7} and ‘M’ = 3, ‘B’ = {2, 3, 6}. 
We can merge these two arrays into {1, 2, 3, 4, 5, 6, 7} (The elements of ‘A’ are {1, 2, 3, 4} ).
Hence, the answer is {1, 2, 3, 4, 5, 6, 7}.

Detailed explanation ( Input/output format, Notes, Images )
Sample Input 1:

3 4
1 8 8
2 3 4 5

Sample Output 1:
1 2 3 4 5 8 8

Explanation Of Sample Input 1:
We have ‘A’ = {1, 8, 8} and ‘B’ = {2, 3, 4, 5}. 
Merging the two arrays results in {1, 2, 3, 4, 5, 8, 8}.
Hence the answer is {1, 2, 3, 4, 5, 8, 8}, where ‘A’ contains {1, 2, 3} and ‘B’ contains {4, 5, 8, 8}.

Sample Input 2:
4 5
1 1 1 1 
2 2 3 3 5

Sample Output 2:
1 1 1 1 2 2 3 3 5

Solution Reference: https://www.geeksforgeeks.org/merge-two-sorted-arrays-o1-extra-space/


Solution 1: Using Insert of Insertion Sort
Time Complexity: O(m * n), where n and m are sizes of a[] and b[] respectively.
Auxiliary Space: O(1)

def mergeTwoSortedArraysWithoutExtraSpace(a : List[int], b : List[int]) -> int:
    for i in range(len(b) - 1, -1, -1):
        if a[-1] > b[i]:
            last = a[-1]
            j = len(a) - 2
            while j >= 0 and a[j] > b[i]:
                a[j + 1] = a[j]
                j -= 1
            
            a[j + 1] = b[i]
            b[i] = last


Solution 2: By Swap and Sort
Time Complexity: O(min(n, m)) + O(n*logn) + O(m*logm), where n and m are the sizes of the given arrays.
Reason: O(min(n, m)) is for swapping the array elements. And O(n*logn) and O(m*logm) are for sorting the two arrays.

Space Complexity: O(1) as we are not using any extra space.

def mergeTwoSortedArraysWithoutExtraSpace(a : List[int], b : List[int]) -> int:
    n=len(a)
    m=len(b)
    left = n - 1
    right = 0

    # Swap the elements until arr1[left] is smaller than arr2[right]:
    while left >= 0 and right < m:
        if a[left] > b[right]:
            a[left], b[right] = b[right], a[left]
            left -= 1
            right += 1
        else:
            break

    # Sort arr1[] and arr2[] individually:
    a.sort()
    b.sort()



Solution 3:  Using gap method): 
This gap method is based on a sorting technique called shell sort. The intuition of this method is simple. 

Time Complexity: O((n+m)*log(n+m)), where n and m are the sizes of the given arrays.
Reason: The gap is ranging from n+m to 1 and every time the gap gets divided by 2. So, the time complexity of the outer loop will be O(log(n+m)). Now, for each value of the gap, the inner loop can at most run for (n+m) times. So, the time complexity of the inner loop will be O(n+m). So, the overall time complexity will be O((n+m)*log(n+m)).

Space Complexity: O(1) as we are not using any extra space.


            
